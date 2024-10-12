import io
import requests
from pypdf import PdfReader
from typing import AnyStr
from gentopia.tools.basetool import *
from pydantic import BaseModel, Field


class ExtractPdfArgs(BaseModel):
    pdf_url: str = Field(..., description="The URL of the PDF file to extract text from.")


class ExtractPdf(BaseTool):
    name = "extract_pdf"
    description = "A tool that extracts the text from a PDF file given its URL."
    args_schema: Optional[Type[BaseModel]] = ExtractPdfArgs

    def _run(self, pdf_url: AnyStr) -> str:
        response = requests.get(pdf_url)
        pdf_file = io.BytesIO(response.content)
        reader = PdfReader(pdf_file)
        text = " ".join(page.extract_text() for page in reader.pages)
        return text

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError