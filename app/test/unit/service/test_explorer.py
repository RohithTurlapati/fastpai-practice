from models.explorer import Explorer
import service.explorer as service


sample = Explorer(name="naveen",
             country="india",
             description="explorer"
             )

def test_create():
    resp = service.create(sample)
    assert resp == sample

def test_get_exists():
    resp = service.get_one(sample.name)
    assert resp == sample

def test_get_missing():
    resp = service.get_one("dsfdsg")
    assert resp == None