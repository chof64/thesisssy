"""
"""

import json


class GetInformation:
    """ """

    async def get_specific_information(json_data: dict):
        """"""

        # convert json string to dict
        data = json.loads(json_data)
        clean = {}
        # TODO: dynamic mapping with a json mapping config file.
        clean["personal_information"] = {
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
            "residential_street": data["Unnamed: 11"]["15"],
            "residential_subdivision": data["Unnamed: 8"]["17"],
            "residential_barangay": data["Unnamed: 11"]["17"],
            "residential_city": data["Unnamed: 8"]["20"],
            "residential_province": data["Unnamed: 11"]["20"],
            "residential_zip_code": data["Unnamed: 8"]["22"],
            "permanent_house_block": data["Unnamed: 8"]["23"],
            "permanent_street": data["Unnamed: 11"]["23"],
            "permanent_subdivision": data["Unnamed: 8"]["25"],
            "permanent_barangay": data["Unnamed: 11"]["25"],
            "permanent_city": data["Unnamed: 8"]["27"],
            "permanent_province": data["Unnamed: 11"]["27"],
            "permanent_zip_code": data["Unnamed: 8"]["29"],
            "telephone_no": data["Unnamed: 8"]["30"],
            "mobile_no": data["Unnamed: 8"]["31"],
            "email_address": data["Unnamed: 8"]["32"],
        }

        clean["family_background"] = {}

        return clean
