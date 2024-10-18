import psutil
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import random
import time

router = APIRouter()

class SystemMetrics(BaseModel):
    cpu_usage: float
    memory_usage: float
    disk_usage: float

class DeploymentStatus(BaseModel):
    status: str
    progress: int
    details: str

class LogEntry(BaseModel):
    timestamp: str
    level: str
    message: str

class Config(BaseModel):
    key: str
    value: str

@router.get("/metrics", response_model=SystemMetrics)
async def get_system_metrics():
    return SystemMetrics(
        cpu_usage=psutil.cpu_percent(),
        memory_usage=psutil.virtual_memory().percent,
        disk_usage=psutil.disk_usage('/').percent
    )

@router.post("/deploy", response_model=DeploymentStatus)
async def simulate_deployment():
    # Simulamos un despliegue que toma tiempo
    for i in range(5):
        time.sleep(1)  # Simulamos trabajo
    
    success = random.choice([True, False])
    if success:
        return DeploymentStatus(
            status="success",
            progress=100,
            details="Deployment completed successfully"
        )
    else:
        raise HTTPException(status_code=500, detail="Deployment failed")

@router.get("/logs", response_model=List[LogEntry])
async def get_logs(limit: int = 10):
    # Simulamos la obtención de logs
    log_levels = ["INFO", "WARNING", "ERROR"]
    logs = [
        LogEntry(
            timestamp=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - i*60)),
            level=random.choice(log_levels),
            message=f"Log entry {i+1}"
        )
        for i in range(limit)
    ]
    return logs

@router.get("/config", response_model=Dict[str, str])
async def get_config():
    # Simulamos la obtención de configuraciones
    return {
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "APP_ENV": "production"
    }

@router.post("/config", response_model=Config)
async def update_config(config: Config):
    # Simulamos la actualización de una configuración
    # En un caso real, aquí actualizaríamos la configuración en una base de datos o archivo
    return config