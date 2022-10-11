"""
"""

import json


class GetInformation:
    """ """

    async def get_specific_information(json_data: dict):
        """"""

        # convert json string to dict
        data = json.loads(json_data)

        clean = {
            "personal_information": {
                "surname": data["Unnamed: 3"]["8"],
                "first_name": data["Unnamed: 3"]["9"],
                "middle_name": data["Unnamed: 3"]["10"],
                "date_of_birth": data["Unnamed: 3"]["11"],
                "place_of_birth": data["Unnamed: 3"]["13"],
                "height": data["Unnamed: 3"]["20"],
                "weight": data["Unnamed: 3"]["22"],
                "blood_type": data["Unnamed: 3"]["23"],
                "gsis_id_no": data["Unnamed: 3"]["25"],
                "pagibig_id_no": data["Unnamed: 3"]["27"],
                "philhealth_no": data["Unnamed: 3"]["29"],
                "sss_no": data["Unnamed: 3"]["30"],
                "tin": data["Unnamed: 3"]["31"],
                "agency_employee_no": data["Unnamed: 3"]["32"],
                "residential_house_block": data["Unnamed: 8"]["15"],
                "residential_street": "",
                "residential_subdivision": data["Unnamed: 8"]["17"],
                "residential_barangay": "",
                "residential_city": "",
                "residential_province": "",
                "residential_zip_code": "",
                "permanent_house_block": "",
                "permanent_street": "",
                "permanent_subdivision": "",
                "permanent_barangay": "",
                "permanent_city": "",
                "permanent_province": "",
                "permanent_zip_code": "",
            }
        }

        return clean
