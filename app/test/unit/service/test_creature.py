from models.creature import Creature
import service.creature as code


sample = Creature(name="rohith",
             country="india",
             area="hastinapuram",
             description="creature",
             aka="psychopragrammer")


def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_get_exists():
    resp = code.get_one(sample.name)
    assert resp == sample

def test_get_missing():
    resp = code.get_one("sfgfad")
    assert resp is None