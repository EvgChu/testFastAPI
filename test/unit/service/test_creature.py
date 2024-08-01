from src.model.creature import Creature
from src.service import creature as code


sample = Creature(
    name="Goblin",
    aka="aka Goblin",
    country="CN",
    area="Himalayes",
    description="Goblin is a very dangerous creature.",
)


def test_create():
    resp = code.create(sample)
    assert resp == sample
   
    
def test_get_exists():
    resp = code.get_one(sample.name)
    assert resp == sample
  
    
def test_get_missing():
    resp = code.get_one("abra")
    assert resp is None
