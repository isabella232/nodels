from nodels.instances import Instances


def test_to_dict():
    i = Instances()
    assert i.to_dict() == {}

    i2 = Instances(data={"foo": "bar"})
    assert i2.to_dict() == {"foo": "bar"}


def test_json():
    i = Instances()
    assert i.json() == "{}"

    i2 = Instances(data={"foo": "bar"})
    assert i2.json() == '{"foo": "bar"}'