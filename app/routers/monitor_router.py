import logging

from fastapi import APIRouter, HTTPException

from ..models.ComparisonAnalysisRequest import ComparisonAnalysisRequest
from ..models.MonitoringResponse import MonitoringResponse
from ..models.SimplificationRequest import SimplificationRequest
from ..models.TextAnalysisRequest import TextAnalysisRequest
from ..services.saving_service import SavingService

# Initialize logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/text-analysis", response_model=MonitoringResponse)
async def store_text_analysis_result(request: TextAnalysisRequest):
    """
    Stores the result of a text analysis operation.
    """
    try:
        logger.info(f"Storing text analysis result: {request}")

        # Save the text analysis request
        analysis_id = await SavingService.save_text_analysis(request.text)

        # Return the analysis_id
        return MonitoringResponse(monitoring_id=analysis_id)
    except Exception as exception:
        logger.exception("Failed to store text analysis result.")
        raise HTTPException(status_code=500, detail="Failed to store text analysis result.")


@router.post("/comparison-analysis", response_model=MonitoringResponse)
async def store_comparison_analysis_result(request: ComparisonAnalysisRequest):
    try:
        logger.info(f"Storing comparison analysis result: {request}")

        # Save the comparison request
        analysis_id = await SavingService.save_comparison_analysis(request.text1, request.text2)

        # Return the analysis_id
        return MonitoringResponse(monitoring_id=analysis_id)
    except Exception as exception:
        logger.exception("Failed to store comparison analysis result.")
        raise HTTPException(status_code=500, detail="Failed to store comparison analysis result.")


@router.post("/text-simplification", response_model=MonitoringResponse)
async def store_text_simplification_result(request: SimplificationRequest):
    try:
        logger.info(f"Storing text simplification result: {request}")

        # Save the comparison request
        simplification_id = await SavingService.save_simplification(request)

        # Return the simplification_id
        return MonitoringResponse(monitoring_id=simplification_id)
    except Exception as exception:
        logger.exception("Failed to store text simplification result.")
        raise HTTPException(status_code=500, detail="Failed to store text simplification result.")
