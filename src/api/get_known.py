from cve_file_connector import LoadCvesFile
from fastapi import APIRouter, HTTPException, Query

router = APIRouter(tags=["Get pages"])

@router.get("/get/known")           # Виводить 10 CVE які були використані в атаках
def GetKnown():
    try:
        def GetKnownRansomwareUse():
            try:
                cveJsonDump = LoadCvesFile()

                filtredVulns = []
                
                for vulnerability in cveJsonDump['vulnerabilities']:
                    if vulnerability['knownRansomwareCampaignUse'].lower() == "known":
                        filtredVulns.append(vulnerability)
                    if len(filtredVulns) >= 10:
                        break

                return filtredVulns
            
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error processing file: {e}")
        
        result = GetKnownRansomwareUse()

        if not result:
            raise HTTPException(status_code=404, detail="No vulnerabilities found related to ransomware campaigns")
        return {"ansomware campaigns were used ": result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")

