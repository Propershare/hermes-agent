"""Seshat runtime branding helpers for the Maat governance fork."""

from __future__ import annotations

import os


def is_seshat_runtime() -> bool:
    return os.getenv("SESHAT_RUNTIME", "").lower() in {"1", "true", "yes", "on"}


def project_name(default: str = "Hermes Agent") -> str:
    return "Seshat" if is_seshat_runtime() else default


def response_label(default: str = "Hermes") -> str:
    return "Seshat" if is_seshat_runtime() else default


def creator_label(default: str = "Nous Research") -> str:
    return "Maat Governance" if is_seshat_runtime() else default


def welcome(default: str) -> str:
    if not is_seshat_runtime():
        return default
    return "Welcome to Seshat. Maat-governed local scholar runtime is active. Type your message or /help for commands."
