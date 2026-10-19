import unittest
from alert_validator import validate_alert

class TestAlertValidator(unittest.TestCase):
    def setUp(self):
        self.alert = {"alert_id":"SOC-001","event_id":4625,"username":"alex.morgan","failed_attempts":12,"source_ip":"203.0.113.25"}
    def test_valid_alert(self):
        self.assertTrue(validate_alert(self.alert)[0])
    def test_missing_source_ip(self):
        self.alert.pop("source_ip")
        valid, message = validate_alert(self.alert)
        self.assertFalse(valid)
        self.assertIn("source_ip", message)
    def test_invalid_failed_attempts(self):
        self.alert["failed_attempts"] = "twelve"
        self.assertFalse(validate_alert(self.alert)[0])
    def test_negative_failed_attempts(self):
        self.alert["failed_attempts"] = -5
        self.assertFalse(validate_alert(self.alert)[0])
    def test_boolean_event_id(self):
        self.alert["event_id"] = True
        self.assertFalse(validate_alert(self.alert)[0])
    def test_invalid_alert_structure(self):
        self.assertFalse(validate_alert(["not","an","alert"])[0])

if __name__ == "__main__":
    unittest.main(verbosity=2)
