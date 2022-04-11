
from Packets.Messages.Client.Login.ClientHelloMessage import ClientHelloMessage
from Packets.Messages.Client.Login.LoginMessage import LoginMessage

from Packets.Messages.Client.Home.KeepAliveMessage import KeepAliveMessage

### TODO ###
from Packets.Messages.Client.Battle.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage

from Packets.Messages.Client.Home.GetPlayerProfileMessage import GetPlayerProfileMessage

AvailablePackets = {
    10100: ClientHelloMessage,
    18101: LoginMessage,
    10108: KeepAliveMessage,
    
    14109: GoHomeFromOfflinePractiseMessage,
    14113: GetPlayerProfileMessage,
}
