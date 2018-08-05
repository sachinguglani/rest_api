from datetime import datetime
from flask import (
    make_response,
    abort
)


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Feed to our API
ENTITY = {
    "key1": {
        "name": "value1",
        "place": "key1",
        "timestamp": get_timestamp()
    },
    "key2": {
        "name": "value2",
        "place": "key2",
        "timestamp": get_timestamp()
    },
    "key3": {
        "name": "value3",
        "place": "key3",
        "timestamp": get_timestamp()
    }
}


def read_all():
    """
    :return:  json string all feeds
    """
    return [ENTITY[key] for key in sorted(ENTITY.keys())]


def read_one(place):
    """
    This function responds /api/entity/{place}
    :param place:   place to find
    :return:        entity matching
    """

    if place in ENTITY:
        entity = ENTITY.get(place)

    else:
        abort(404, 'Entity with  {place} doesnt exist'.format(
            place=place))

    return entity


def create(entity):
    """
    :param entity:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    place = entity.get('place', None)
    name = entity.get('name', None)

    # Does the person exist already?
    if place not in ENTITY and place is not None:
        ENTITY[place] = {
            'place': place,
            'name': name,
            "timestamp": get_timestamp()
        }
        return make_response('{place} successfully created'.format(
            place=place), 201)

    else:
        abort(406, 'Entity with {place} already exists'.format(
            place=place))


def update(place, entity):
    """
    This function updates an existing structure
    :param place:   place to update
    :param entity:  entity to update
    :return:        updated structure
    """
    if place in ENTITY:
        ENTITY[place]['name'] = entity.get('name')
        ENTITY[place]['timestamp'] = get_timestamp()

        return ENTITY[place]

    else:
        abort(404, 'Entity with {place} not found'.format(
            place=place))


def delete(place):
    """
    This function deletes an entity
    :param place:   place to delete
    :return:        200 on successful delete, 404 if not found
    """

    if place in ENTITY:
        del ENTITY[place]
        return make_response('{place} successfully deleted'.format(
            place=place), 200)

    else:
        abort(404, 'Entity with {place} not found'.format(
            place=place))
