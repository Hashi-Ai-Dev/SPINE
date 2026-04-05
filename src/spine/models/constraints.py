"""Pydantic v2 model for .spine/constraints.yaml"""

from __future__ import annotations

from typing import Any

import yaml
from pydantic import BaseModel, Field


class WorkSchedule(BaseModel):
    timezone: str = "America/New_York"
    blocked_windows: list[Any] = Field(default_factory=list)

    model_config = {"extra": "allow"}


class ParallelLimits(BaseModel):
    max_active_missions: int = 1
    max_concurrent_runs: int = 2


class Budget(BaseModel):
    monthly_usd_soft_cap: int = 0


class RoutingPreferences(BaseModel):
    use_local_for: list[str] = Field(default_factory=list)
    use_frontier_for: list[str] = Field(default_factory=list)


class BehaviorRules(BaseModel):
    require_plan_for_complex_tasks: bool = True
    block_scope_expansion_without_decision: bool = True
    require_evidence_for_weekly_review: bool = True


class ConstraintsModel(BaseModel):
    version: int = Field(default=1, frozen=True)
    profile_name: str = "default"
    work_schedule: WorkSchedule = Field(default_factory=WorkSchedule)
    build_windows: dict[str, Any] = Field(default_factory=dict)
    parallel_limits: ParallelLimits = Field(default_factory=ParallelLimits)
    budget: Budget = Field(default_factory=Budget)
    routing_preferences: RoutingPreferences = Field(default_factory=RoutingPreferences)
    behavior_rules: BehaviorRules = Field(default_factory=BehaviorRules)

    model_config = {"extra": "forbid"}

    def to_yaml(self) -> str:
        data = self.model_dump(mode="python")
        return yaml.dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True)

    @classmethod
    def from_yaml(cls, raw: str) -> "ConstraintsModel":
        data = yaml.safe_load(raw)
        return cls.model_validate(data)
