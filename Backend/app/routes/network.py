from fastapi import APIRouter, HTTPException
import json
import numpy as np
from starlette.responses import JSONResponse
import logging
import sys
from app.models import NetworkData

from app.services import (
    fetch_gene_network,
    create_network_graph,
    calculate_metrics,
    remove_gene,
    modify_edge_weight
)
from app.models import Interaction, NetworkMetrics, RemoveGeneRequest, ModifyEdgeRequest

router = APIRouter()

# Global variable for storing the network graph
G = None
print("🚀 This is a fresh execution of fetch_network()")
 # Forces output to appear in terminal

logging.info("🔥 Fetch network function is running!")


logging.basicConfig(level=logging.INFO)
