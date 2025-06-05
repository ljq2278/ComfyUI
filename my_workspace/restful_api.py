import asyncio
import logging
import httpx
import inspect
import base64
import json
import aiohttp
# from sseclient import SSEClient
from aiohttp_sse_client import client as sse_client

timeout_settings = aiohttp.ClientTimeout(
    total=None,  # No total timeout for the entire operation (SSE is long-lived)
    connect=1,  # 10 seconds to connect
    sock_connect=1,  # 5 seconds for socket connection part of connect
    sock_read=1    # 10 seconds to wait for data from the server on the socket
    # If the server doesn't send anything (even comments) for 10s,
    # this will fire.
)


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


class OpenAIBaseInterface:

    def _get_res(self, response, tpe):
        ret = {}
        if tpe == "message":
            obj = response["choices"][0]["message"]
        else:
            obj = response["choices"][0]["delta"]
        if "tool_calls" in obj and obj["tool_calls"] is not None:
            ret["func"] = [{"name": "", "arguments": ""} for _ in range(0, len(obj["tool_calls"]))]
            for i in range(0, len(obj["tool_calls"])):
                itm = obj["tool_calls"][i]
                ret["func"][i]["name"] = itm["function"]["name"]
                ret["func"][i]["arguments"] = itm["function"]["arguments"]
        if "content" in obj and obj["content"] is not None:
            ret["text"] = obj["content"]
        if "reasoning_content" in obj and obj["reasoning_content"] is not None:
            ret["think"] = obj["reasoning_content"]
        return ret

    def _set_message(self, chat_content_dict, chat_content, history, prompt, img_urls, img_paths, img_base64_utf8s):
        dialoags = []
        if prompt:
            dialoags.append({"role": "system", "content": prompt})
        dialoags.extend([{"role": "assistant", "content": x["content"]} if x["role"] == "ai" else x for x in history])
        if chat_content_dict:
            dialoags.append(chat_content_dict)
        content = []
        if chat_content:
            content.append({"type": "text", "text": chat_content})
        if img_urls:
            for img_url in img_urls:
                content.append({"type": "image_url", "image_url": {"url": img_url}})
        if img_paths:
            for img_path in img_paths:
                base64_image = encode_image(img_path)
                content.append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}})
        if img_base64_utf8s:
            for img_base64_utf8 in img_base64_utf8s:
                content.append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64_utf8}"}})
        if len(content) > 0:
            dialoags.append({"role": "user", "content": content})
        return dialoags

    async def async_chat(self,
                         chat_content,
                         history,
                         prompt=None,
                         max_length=256,
                         temperature=0.1,
                         request_id=0,
                         uid=0,
                         presence_penalty=0.0,
                         frequency_penalty=0.0,
                         tools=None,
                         img_urls=None,
                         img_paths=None,
                         img_base64_utf8s=None,
                         chat_content_dict=None,
                         **kwargs
                         ):
        dialoags = self._set_message(chat_content_dict, chat_content, history, prompt, img_urls, img_paths, img_base64_utf8s)
        payload = {
            "model": self.engine,
            "messages": dialoags,
            "stream": False,
            "temperature": temperature,
            "max_tokens": max_length,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty,
            "tools": tools,
            "enable_thinking": kwargs.get("enable_thinking", False),
        }

        # url = f"{self.azure_endpoint}openai/deployments/{self.engine}/chat/completions?api-version={self.api_version}"
        response = await self.http_client.post(self.url, headers=self.headers, json=payload, imeout=kwargs.get("timeout", 20))
        res = self._get_res(json.loads(response.text), "message")
        # logging.info(f"debug request_id:{request_id} uid:{uid} {type(self)} {inspect.currentframe().f_code.co_name} res: {res}")
        return res

    async def async_stream_chat(self,
                                chat_content,
                                history,
                                prompt=None,
                                max_length=256,
                                temperature=0.1,
                                request_id=0,
                                uid=0,
                                presence_penalty=0.0,
                                frequency_penalty=0.0,
                                tools=None,
                                img_urls=None,
                                img_paths=None,
                                img_base64_utf8s=None,
                                chat_content_dict=None,
                                **kwargs
                                ):
        dialoags = self._set_message(chat_content_dict, chat_content, history, prompt, img_urls, img_paths, img_base64_utf8s)
        payload = {
            "model": self.engine,
            "messages": dialoags,
            "stream": True,
            "temperature": temperature,
            "max_tokens": max_length,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty,
            "tools": tools,
            "enable_thinking": kwargs.get("enable_thinking", False),
        }
        
        async with sse_client.EventSource(self.url, option={"method": "POST"}, headers=self.headers, json=payload) as response:
            async for event in response:
                if event.data == "[DONE]":
                    return
                res = self._get_res(json.loads(event.data), "delta")
                yield res


class ChatGPT4O(OpenAIBaseInterface):
    def __init__(self, **kwargs):
        self.ai_nm = "assistant"
        for k, v in kwargs.items():
            if k == "gpt4o_key":
                self.api_key = v
            if k == "gpt4o_version":
                self.api_version = v
            if k == "gpt4o_engine":
                self.engine = v
            if k == "gpt4o_base":
                self.azure_endpoint = v
        self.url = f"{self.azure_endpoint}openai/deployments/{self.engine}/chat/completions?api-version={self.api_version}"
        self.headers = {
            "api-key": f"{self.api_key}",
        }


class ChatGPT4Turbo(OpenAIBaseInterface):
    def __init__(self, **kwargs):
        self.ai_nm = "assistant"
        for k, v in kwargs.items():
            if k == "gpt4tubor_key":
                self.api_key = v
            if k == "gpt4tubor_version":
                self.api_version = v
            if k == "gpt4tubor_engine":
                self.engine = v
            if k == "gpt4tubor_base":
                self.azure_endpoint = v
        self.http_client = kwargs["http_client"]
        self.url = f"{self.azure_endpoint}openai/deployments/{self.engine}/chat/completions?api-version={self.api_version}"
        self.headers = {
            "api-key": f"{self.api_key}",
        }


class Deepseek(OpenAIBaseInterface):
    def __init__(self, **kwargs):
        self.ai_nm = "assistant"
        for k, v in kwargs.items():
            if k == "deepseek_api_key":
                self.api_key = v
            if k == "deepseek_engine":
                self.engine = v
            if k == "deepseek_url":
                self.base_url = v
        self.http_client = kwargs["http_client"]
        self.url = f"{self.base_url}/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }


class QianwenClient(OpenAIBaseInterface):
    def __init__(self, **kwargs):
        self.engine = kwargs["qianwen_engine"]
        self.api_key = kwargs["qianwen_api_key"]
        self.base_url = kwargs["qianwen_url"]
        self.http_client = kwargs["http_client"]
        self.url = f"{self.base_url}/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }


class OpenaiClient(OpenAIBaseInterface):
    def __init__(self, **kwargs):
        self.ai_nm = "assistant"
        for k, v in kwargs.items():
            if k == "api_key":
                self.api_key = v
            if k == "engine":
                self.engine = v
            if k == "url":
                self.base_url = v
        self.http_client = kwargs["http_client"]
        self.url = f"{self.base_url}/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
