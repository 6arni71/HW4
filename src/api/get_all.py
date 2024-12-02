import datetime
from cve_file_connector import LoadCvesFile
from fastapi import APIRouter, HTTPException, Query

router = APIRouter(tags=["Get pages"])

@router.get("/get/all")             # Виводить CVE за останні n днів. Максимум 40 CVE
def GetAll(daysCount: int = Query(5, ge=1, le=365)):
    try:
        def GetAllCveLastFiveDays():

            cveJsonDump = LoadCvesFile()

            dateFiveDaysAgo = datetime.date.today() - datetime.timedelta(days=daysCount)

            filtredVulns = []

            for vulnerability in cveJsonDump['vulnerabilities']:
                if 'dateAdded' in vulnerability:
                    dateAdded = datetime.datetime.strptime(vulnerability['dateAdded'], "%Y-%m-%d").date()
                    if dateAdded >= dateFiveDaysAgo:
                        filtredVulns.append(vulnerability)
                        if len(filtredVulns) > 40:
                            break

                return filtredVulns
            
        result = GetAllCveLastFiveDays()

        if not result:
            raise HTTPException(status_code=404, detail=f"No vulnerabilities found for the last {daysCount} days")
        return {f"Vulnerabilities for the last {daysCount} days": result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
