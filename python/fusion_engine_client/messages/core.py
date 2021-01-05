from .defs import *
from .measurements import *
from .solution import *
from .ros import *

message_type_to_class = {
    PoseMessage.MESSAGE_TYPE: PoseMessage,
    PoseAuxMessage.MESSAGE_TYPE: PoseAuxMessage,
    GNSSInfoMessage.MESSAGE_TYPE: GNSSInfoMessage,
    GNSSSatelliteMessage.MESSAGE_TYPE: GNSSSatelliteMessage,
    IMUMeasurement.MESSAGE_TYPE: IMUMeasurement,
    ROS_PoseMessage.MESSAGE_TYPE: ROS_PoseMessage,
    ROS_GPSFixMessage.MESSAGE_TYPE: ROS_GPSFixMessage,
    ROS_IMUMessage.MESSAGE_TYPE: ROS_IMUMessage
}
