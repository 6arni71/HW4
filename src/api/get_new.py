from cve_file_connector import LoadCvesFile
from fastapi import APIRouter, HTTPException, Query

router = APIRouter(tags=["Get pages"])

@router.get("/get/new")                 # Виводить 10 найновіших CVE
def GetNew():
    try:
        def GetTenNewVulnerabilities():
            cveJsonDump = LoadCvesFile()

            filtredVulns = []

            for vulnerability in cveJsonDump['vulnerabilities']:
                filtredVulns.append(vulnerability)
                if len(filtredVulns) >= 10:
                    break

            return filtredVulns
        
        result = GetTenNewVulnerabilities()

        return {"10 newest vulnerabilities": result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
