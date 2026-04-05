"""Pydantic v2 model for .spine/mission.yaml"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal

import yaml
from pydantic import BaseModel, Field


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class SuccessMetric(BaseModel):
    type: Literal["milestone", "metric", "user_signal"] = "milestone"
    value: str = ""


class MissionModel(BaseModel):
    version: int = Field(default=1, frozen=True)
    id: str = Field(default="mission-0001")
    title: str = "Define active mission"
    status: Literal["active", "paused", "complete", "killed"] = "active"
    target_user: str = ""
    user_problem: str = ""
    one_sentence_promise: str = ""
    success_metric: SuccessMetric = Field(default_factory=SuccessMetric)
    deadline_window_days: int = 42
    review_cadence: Literal["daily", "weekly", "biweekly"] = "weekly"
    preferred_runtimes: list[str] = Field(default_factory=list)
    preferred_models: dict[str, Any] = Field(default_factory=dict)
    allowed_scope: list[str] = Field(default_factory=list)
    forbidden_expansions: list[str] = Field(default_factory=list)
    proof_requirements: list[str] = Field(default_factory=list)
    kill_conditions: list[str] = Field(default_factory=list)
    created_at: str = Field(default_factory=_now_iso)
    updated_at: str = Field(default_factory=_now_iso)

    model_config = {"extra": "forbid"}

    def to_yaml(self) -> str:
        data = self.model_dump(mode="python")
        return yaml.dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True)

    @classmethod
    def from_yaml(cls, raw: str) -> "MissionModel":
        data = yaml.safe_load(raw)
        return cls.model_validate(data)
