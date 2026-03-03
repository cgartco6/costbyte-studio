def check_popia_compliance(data_processing: dict):
    # Stub: Check consent, minimization
    if not data_processing.get("consent_given"):
        raise ValueError("POPIA violation: No consent")
    # GDPR alignment: Check data residency
    if data_processing.get("eu_user"):
        print("Ensure EU data boundary")
    return True
