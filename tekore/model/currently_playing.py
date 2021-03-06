from typing import Optional
from dataclasses import dataclass

from tekore.serialise import SerialisableDataclass, SerialisableEnum
from tekore.model.context import Context
from tekore.model.device import Device
from tekore.model.track import FullTrack


class CurrentlyPlayingType(SerialisableEnum):
    ad = 'ad'
    episode = 'episode'
    track = 'track'
    unknown = 'unknown'


class RepeatState(SerialisableEnum):
    off = 'off'
    track = 'track'
    context = 'context'


@dataclass
class Disallows(SerialisableDataclass):
    interrupting_playback: bool = False
    pausing: bool = False
    resuming: bool = False
    seeking: bool = False
    skipping_next: bool = False
    skipping_prev: bool = False
    toggling_repeat_context: bool = False
    toggling_shuffle: bool = False
    toggling_repeat_track: bool = False
    transferring_playback: bool = False


@dataclass
class Actions(SerialisableDataclass):
    disallows: Disallows

    def __post_init__(self):
        self.disallows = Disallows(**self.disallows)


@dataclass
class CurrentlyPlaying(SerialisableDataclass):
    """
    Context, progress_ms and item may be None e.g. during a private session.
    """
    actions: Actions
    currently_playing_type: CurrentlyPlayingType
    is_playing: bool
    timestamp: int
    context: Optional[Context]
    progress_ms: Optional[int]
    item: Optional[FullTrack]

    def __post_init__(self):
        self.actions = Actions(**self.actions)
        self.currently_playing_type = CurrentlyPlayingType[
            self.currently_playing_type
        ]

        if self.context is not None:
            self.context = Context(**self.context)
        if self.item is not None:
            self.item = FullTrack(**self.item)


@dataclass
class CurrentlyPlayingContext(CurrentlyPlaying):
    device: Device
    repeat_state: RepeatState
    shuffle_state: bool

    def __post_init__(self):
        super().__post_init__()
        self.device = Device(**self.device)
        self.repeat_state = RepeatState[self.repeat_state]
