from cve_file_connector import LoadCvesFile
from fastapi import APIRouter, HTTPException, Query

router = APIRouter(tags=["Get pages"])

@router.get("/get")                     # Виводить CVE які містять ключове слово
def GetQuery(query: str = Query(..., min_length=1)):
    try:
        def GetVulnsByKeywords():

            cveJsonDump = LoadCvesFile()

            filtredVulns = [vuln for vuln in cveJsonDump['vulnerabilities'] if query.lower() in str(vuln).lower()]

            return filtredVulns

        result = GetVulnsByKeywords()

        if not result:
            raise HTTPException(status_code=404, detail=f"No vulnerabilities found containing the keyword '{query}'")
        return {"Vulnerabilities found on query": result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
