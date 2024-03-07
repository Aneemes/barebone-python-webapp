from typing import Iterator
from peer_to_peer.models import User
from peer_to_peer.urls import url_handlers

def app(environ, start_response) -> Iterator[bytes]:
    user = User()
    return iter([url_handlers(environ, start_response, user)])
