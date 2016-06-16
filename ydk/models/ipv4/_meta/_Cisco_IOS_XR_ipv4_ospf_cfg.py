


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'OspfFastRerouteTiebreakersEnum' : _MetaInfoEnum('OspfFastRerouteTiebreakersEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'downstream':'DOWNSTREAM',
            'line-card-disjoint':'LINE_CARD_DISJOINT',
            'lowest-metric':'LOWEST_METRIC',
            'node-protect':'NODE_PROTECT',
            'primary-path':'PRIMARY_PATH',
            'secondary-path':'SECONDARY_PATH',
            'srlg-disjoint':'SRLG_DISJOINT',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfFastRerouteEnum' : _MetaInfoEnum('OspfFastRerouteEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'none':'NONE',
            'per-link':'PER_LINK',
            'per-prefix':'PER_PREFIX',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfRedistLsaEnum' : _MetaInfoEnum('OspfRedistLsaEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'summary':'SUMMARY',
            'external':'EXTERNAL',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfIetfNsfEnum' : _MetaInfoEnum('OspfIetfNsfEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'all':'ALL',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'BfdEnableModeEnum' : _MetaInfoEnum('BfdEnableModeEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'disable':'DISABLE',
            'default':'DEFAULT',
            'strict':'STRICT',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfFastReroutePriorityEnum' : _MetaInfoEnum('OspfFastReroutePriorityEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'critical':'CRITICAL',
            'high':'HIGH',
            'medium':'MEDIUM',
            'low':'LOW',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfCiscoNsfEnum' : _MetaInfoEnum('OspfCiscoNsfEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'always':'ALWAYS',
            'require-nsf-neighbors':'REQUIRE_NSF_NEIGHBORS',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfRedistProtocolEnum' : _MetaInfoEnum('OspfRedistProtocolEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'all':'ALL',
            'connected':'CONNECTED',
            'static':'STATIC',
            'bgp':'BGP',
            'rip':'RIP',
            'isis':'ISIS',
            'ospf':'OSPF',
            'eigrp':'EIGRP',
            'dagr':'DAGR',
            'subscriber':'SUBSCRIBER',
            'application':'APPLICATION',
            'mobile':'MOBILE',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfSegmentRoutingEnum' : _MetaInfoEnum('OspfSegmentRoutingEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'disable':'DISABLE',
            'mpls':'MPLS',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfUloopAvoidanceEnum' : _MetaInfoEnum('OspfUloopAvoidanceEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'protected':'PROTECTED',
            'all':'ALL',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfSegmentRoutingForwardingEnum' : _MetaInfoEnum('OspfSegmentRoutingForwardingEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'disable':'DISABLE',
            'mpls':'MPLS',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfAddressFamilyEnum' : _MetaInfoEnum('OspfAddressFamilyEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'ipv4':'IPV4',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfIetfNsfSupportEnum' : _MetaInfoEnum('OspfIetfNsfSupportEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'never':'NEVER',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfAuthenticationEnum' : _MetaInfoEnum('OspfAuthenticationEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'none':'NONE',
            'plain':'PLAIN',
            'md5':'MD5',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfLogAdjEnum' : _MetaInfoEnum('OspfLogAdjEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'brief':'BRIEF',
            'detail':'DETAIL',
            'suppress':'SUPPRESS',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfSubAddressFamilyEnum' : _MetaInfoEnum('OspfSubAddressFamilyEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'unicast':'UNICAST',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfDomainIdEnum' : _MetaInfoEnum('OspfDomainIdEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'type0005':'TYPE0005',
            'type0105':'TYPE0105',
            'type0205':'TYPE0205',
            'type8005':'TYPE8005',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfEigrpRouteEnum' : _MetaInfoEnum('OspfEigrpRouteEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'internal':'INTERNAL',
            'external':'EXTERNAL',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfSidEnum' : _MetaInfoEnum('OspfSidEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'index':'INDEX',
            'absolute':'ABSOLUTE',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'NsrEnum' : _MetaInfoEnum('NsrEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'true':'TRUE',
            'false':'FALSE',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfLinkStateMetricEnum' : _MetaInfoEnum('OspfLinkStateMetricEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'type1':'TYPE1',
            'type2':'TYPE2',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfDistListProtocolEnum' : _MetaInfoEnum('OspfDistListProtocolEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'all':'ALL',
            'connected':'CONNECTED',
            'static':'STATIC',
            'bgp':'BGP',
            'ospf':'OSPF',
            'dagr':'DAGR',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfRouteLevelEnum' : _MetaInfoEnum('OspfRouteLevelEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'type1':'TYPE1',
            'type2':'TYPE2',
            'type1-and2':'TYPE1_AND2',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfNetworkEnum' : _MetaInfoEnum('OspfNetworkEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'broadcast':'BROADCAST',
            'non-broadcast':'NON_BROADCAST',
            'point-to-point':'POINT_TO_POINT',
            'point-to-multipoint':'POINT_TO_MULTIPOINT',
            'non-broadcast-point-to-multipoint':'NON_BROADCAST_POINT_TO_MULTIPOINT',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfFrrRlfaTunnelEnum' : _MetaInfoEnum('OspfFrrRlfaTunnelEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'none':'NONE',
            'mpls-ldp':'MPLS_LDP',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfShutdownEnum' : _MetaInfoEnum('OspfShutdownEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'full':'FULL',
            'hostmode':'HOSTMODE',
            'onreload':'ONRELOAD',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'OspfKeychainAuthEnum' : _MetaInfoEnum('OspfKeychainAuthEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg',
        {
            'none':'NONE',
            'keychain':'KEYCHAIN',
        }, 'Cisco-IOS-XR-ipv4-ospf-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg']),
    'Ospf.Processes.Process.Snmp.TrapRateLimit' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Snmp.TrapRateLimit',
            False, 
            [
            _MetaInfoClassMember('max-window-traps', ATTRIBUTE, 'int' , None, None, 
                [(0, 300)], [], 
                '''                Max number of traps to send in window time
                ''',
                'max_window_traps',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('window-size', ATTRIBUTE, 'int' , None, None, 
                [(2, 60)], [], 
                '''                Trap rate limit sliding window size
                ''',
                'window_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'trap-rate-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Snmp' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Snmp',
            False, 
            [
            _MetaInfoClassMember('trap-rate-limit', REFERENCE_CLASS, 'TrapRateLimit' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Snmp.TrapRateLimit', 
                [], [], 
                '''                Per OSPF process SNMP trap rate-limit
                ''',
                'trap_rate_limit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'snmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Distribute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Distribute',
            False, 
            [
            _MetaInfoClassMember('instance-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Instance ID
                ''',
                'instance_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('throttle', ATTRIBUTE, 'int' , None, None, 
                [(1, 3600)], [], 
                '''                Seconds
                ''',
                'throttle',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.DomainId.PrimaryDomainId' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.DomainId.PrimaryDomainId',
            False, 
            [
            _MetaInfoClassMember('domain-id-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Primary domain ID value
                ''',
                'domain_id_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('domain-id-type', REFERENCE_ENUM_CLASS, 'OspfDomainIdEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfDomainIdEnum', 
                [], [], 
                '''                Primary domain ID type
                ''',
                'domain_id_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'primary-domain-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds.SecondaryDomainId' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds.SecondaryDomainId',
            False, 
            [
            _MetaInfoClassMember('domain-id-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Secondary domain ID value
                ''',
                'domain_id_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('domain-id-type', REFERENCE_ENUM_CLASS, 'OspfDomainIdEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfDomainIdEnum', 
                [], [], 
                '''                Secondary domain ID type
                ''',
                'domain_id_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'secondary-domain-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds',
            False, 
            [
            _MetaInfoClassMember('secondary-domain-id', REFERENCE_LIST, 'SecondaryDomainId' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds.SecondaryDomainId', 
                [], [], 
                '''                OSPF Secondary domain ID
                ''',
                'secondary_domain_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'secondary-domain-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.DomainId' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.DomainId',
            False, 
            [
            _MetaInfoClassMember('primary-domain-id', REFERENCE_CLASS, 'PrimaryDomainId' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.DomainId.PrimaryDomainId', 
                [], [], 
                '''                OSPF Primary domain ID
                ''',
                'primary_domain_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('secondary-domain-ids', REFERENCE_CLASS, 'SecondaryDomainIds' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds', 
                [], [], 
                '''                Secondary domain ID Table
                ''',
                'secondary_domain_ids',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'domain-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Microloop.Avoidance' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Microloop.Avoidance',
            False, 
            [
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'OspfUloopAvoidanceEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfUloopAvoidanceEnum', 
                [], [], 
                '''                MicroLoop avoidance feature enable
                configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('rib-update-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 600000)], [], 
                '''                Delay to introduce between SPF and RIB update
                in msecs
                ''',
                'rib_update_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'avoidance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Microloop' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Microloop',
            False, 
            [
            _MetaInfoClassMember('avoidance', REFERENCE_CLASS, 'Avoidance' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Microloop.Avoidance', 
                [], [], 
                '''                Microloop avoidance configuration
                ''',
                'avoidance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'microloop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.MaximumRedistributePrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.MaximumRedistributePrefix',
            False, 
            [
            _MetaInfoClassMember('number-of-prefixes', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Maximum number of prefixes redistributed
                ''',
                'number_of_prefixes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Threshold value (%) at which to generate a
                warning msg
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('warning-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only give warning messsage when limit is
                exceeded
                ''',
                'warning_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'maximum-redistribute-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.DefaultInformation' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.DefaultInformation',
            False, 
            [
            _MetaInfoClassMember('always-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Always advertise default route
                ''',
                'always_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                OSPF metric
                ''',
                'metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Routing policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'default-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Af' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'OspfAddressFamilyEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'OspfSubAddressFamilyEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSubAddressFamilyEnum', 
                [], [], 
                '''                Sub-Address family
                ''',
                'saf_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Queue' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Queue',
            False, 
            [
            _MetaInfoClassMember('dispatch-incoming', ATTRIBUTE, 'int' , None, None, 
                [(30, 3000)], [], 
                '''                Maximum number of continuous incoming
                packet-related events processed
                ''',
                'dispatch_incoming',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dispatch-rate-limited', ATTRIBUTE, 'int' , None, None, 
                [(30, 3000)], [], 
                '''                Maximum number of continuous rate-limited LSAs
                processed
                ''',
                'dispatch_rate_limited',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dispatch-rate-limited-flush', ATTRIBUTE, 'int' , None, None, 
                [(30, 3000)], [], 
                '''                Maximum number of continuous rate-limited LSAs
                processed for FLUSH
                ''',
                'dispatch_rate_limited_flush',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dispatch-spf-lsa-limit', ATTRIBUTE, 'int' , None, None, 
                [(30, 3000)], [], 
                '''                Maximum number of continuous summary or
                external LSAs processed
                ''',
                'dispatch_spf_lsa_limit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('limit-high', ATTRIBUTE, 'int' , None, None, 
                [(1000, 30000)], [], 
                '''                Hello events are dropped when incoming event
                queue exceeds this
                ''',
                'limit_high',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('limit-low', ATTRIBUTE, 'int' , None, None, 
                [(1000, 30000)], [], 
                '''                DBDs/Updates are dropped when incoming event
                queue exceeds this
                ''',
                'limit_low',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('limit-medium', ATTRIBUTE, 'int' , None, None, 
                [(1000, 30000)], [], 
                '''                LSA ACKs are dropped when incoming event queue
                exceeds this
                ''',
                'limit_medium',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnProcRestart' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnProcRestart',
            False, 
            [
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override external-lsa metric with max-metric
                value
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in external-LSAs (default
                16711680)
                ''',
                'external_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set maximum metric for stub links in
                router-LSAs
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('startup-max', ATTRIBUTE, 'int' , None, None, 
                [(5, 86400)], [], 
                '''                Time in seconds to originate router-LSA with
                max-metric
                ''',
                'startup_max',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override summary-lsa metric with max-metric
                value
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in summary-LSAs (default
                16711680)
                ''',
                'summary_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Let BGP decide when to originate router-LSA
                with normal metric
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-metric-on-proc-restart',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnStartup' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnStartup',
            False, 
            [
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override external-lsa metric with max-metric
                value
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in external-LSAs (default
                16711680)
                ''',
                'external_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set maximum metric for stub links in
                router-LSAs
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('startup-max', ATTRIBUTE, 'int' , None, None, 
                [(5, 86400)], [], 
                '''                Time in seconds to originate router-LSA with
                max-metric
                ''',
                'startup_max',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override summary-lsa metric with max-metric
                value
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in summary-LSAs (default
                16711680)
                ''',
                'summary_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Let BGP decide when to originate router-LSA
                with normal metric
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-metric-on-startup',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnProcMigration' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnProcMigration',
            False, 
            [
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override external-lsa metric with max-metric
                value
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in external-LSAs (default
                16711680)
                ''',
                'external_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set maximum metric for stub links in
                router-LSAs
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('startup-max', ATTRIBUTE, 'int' , None, None, 
                [(5, 86400)], [], 
                '''                Time in seconds to originate router-LSA with
                max-metric
                ''',
                'startup_max',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override summary-lsa metric with max-metric
                value
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in summary-LSAs (default
                16711680)
                ''',
                'summary_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Let BGP decide when to originate router-LSA
                with normal metric
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-metric-on-proc-migration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricAlways' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricAlways',
            False, 
            [
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override external-lsa metric with max-metric
                value
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in external-LSAs (default
                16711680)
                ''',
                'external_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set maximum metric for stub links in
                router-LSAs
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override summary-lsa metric with max-metric
                value
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in summary-LSAs (default
                16711680)
                ''',
                'summary_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-metric-always',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnSwitchover' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnSwitchover',
            False, 
            [
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override external-lsa metric with max-metric
                value
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in external-LSAs (default
                16711680)
                ''',
                'external_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set maximum metric for stub links in
                router-LSAs
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('startup-max', ATTRIBUTE, 'int' , None, None, 
                [(5, 86400)], [], 
                '''                Time in seconds to originate router-LSA with
                max-metric
                ''',
                'startup_max',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override summary-lsa metric with max-metric
                value
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in summary-LSAs (default
                16711680)
                ''',
                'summary_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Let BGP decide when to originate router-LSA
                with normal metric
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-metric-on-switchover',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.MaxMetric' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.MaxMetric',
            False, 
            [
            _MetaInfoClassMember('max-metric-always', REFERENCE_CLASS, 'MaxMetricAlways' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricAlways', 
                [], [], 
                '''                Set maximum metric always configuration
                ''',
                'max_metric_always',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-metric-no-abr-off', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Block ABR-disable mode entry while in
                max-metric mode
                ''',
                'max_metric_no_abr_off',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-metric-on-proc-migration', REFERENCE_CLASS, 'MaxMetricOnProcMigration' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnProcMigration', 
                [], [], 
                '''                Set maximum metric on-proc-migration
                configuration
                ''',
                'max_metric_on_proc_migration',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-metric-on-proc-restart', REFERENCE_CLASS, 'MaxMetricOnProcRestart' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnProcRestart', 
                [], [], 
                '''                Set maximum metric on-proc-restart
                configuration
                ''',
                'max_metric_on_proc_restart',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-metric-on-startup', REFERENCE_CLASS, 'MaxMetricOnStartup' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnStartup', 
                [], [], 
                '''                Set maximum metric on-startup configuration
                ''',
                'max_metric_on_startup',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-metric-on-switchover', REFERENCE_CLASS, 'MaxMetricOnSwitchover' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnSwitchover', 
                [], [], 
                '''                Set maximum metric on-switchover configuration
                ''',
                'max_metric_on_switchover',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-metric',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Nsf' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Nsf',
            False, 
            [
            _MetaInfoClassMember('cisco', REFERENCE_ENUM_CLASS, 'OspfCiscoNsfEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfCiscoNsfEnum', 
                [], [], 
                '''                Enable Cisco Non Stop Forwarding
                ''',
                'cisco',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('flush-delay-time', ATTRIBUTE, 'int' , None, None, 
                [(1, 3600)], [], 
                '''                Maximum time allowed for external route
                learning (seconds)
                ''',
                'flush_delay_time',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ietf', REFERENCE_ENUM_CLASS, 'OspfIetfNsfEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfIetfNsfEnum', 
                [], [], 
                '''                Enable IETF Non Stop Forwarding
                ''',
                'ietf',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ietf-strict-lsa-checking', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Strict LSA checking of IETF NSF
                ''',
                'ietf_strict_lsa_checking',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ietf-support-role', REFERENCE_ENUM_CLASS, 'OspfIetfNsfSupportEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfIetfNsfSupportEnum', 
                [], [], 
                '''                Disable helper support role for IETF Non Stop
                Forwarding
                ''',
                'ietf_support_role',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(90, 3600)], [], 
                '''                Minimum interval between Non Stop Forwarding
                restarts in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [(90, 1800)], [], 
                '''                Maximum route lifetime following restart in
                seconds
                ''',
                'lifetime',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'nsf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Srgb' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Srgb',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int' , None, None, 
                [(16000, 1048575)], [], 
                '''                The lower bound of the SRGB
                ''',
                'lower_bound',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int' , None, None, 
                [(16000, 1048575)], [], 
                '''                The upper bound of the SRGB
                ''',
                'upper_bound',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'srgb',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 50)], [], 
                '''                Detection multiplier for BFD sessions created
                by OSPF
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'BfdEnableModeEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'BfdEnableModeEnum', 
                [], [], 
                '''                 use of Bidirectional Forwarding Detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(3, 30000)], [], 
                '''                Hello interval for BFD sessions created by OSPF
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Security.Ttl' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Security.Ttl',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable TTL security
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hop-count', ATTRIBUTE, 'int' , None, None, 
                [(1, 254)], [], 
                '''                Hop count
                ''',
                'hop_count',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ttl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Security' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Security',
            False, 
            [
            _MetaInfoClassMember('ttl', REFERENCE_CLASS, 'Ttl' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Security.Ttl', 
                [], [], 
                '''                Enabling turns on TTL security
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'security',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('maximum-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Maximum path cost to remote LFA
                ''',
                'maximum_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tunnel', REFERENCE_ENUM_CLASS, 'OspfFrrRlfaTunnelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFrrRlfaTunnelEnum', 
                [], [], 
                '''                Enable/Disable remote LFA computation
                ''',
                'tunnel',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.RemoteLfa', 
                [], [], 
                '''                Remote LFA configuration
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('topology-independent-lfa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Topology Independet LFA configuration
                ''',
                'topology_independent_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'OspfFastRerouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.ProcessScope',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF demand circuit
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable an OSPF area to advertise
                intra-area prefixes out of this area as external
                ''',
                'external_out',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-auto-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS LDP Auto Config
                ''',
                'ldp_auto_config',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync-igp-shortcuts', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync for igp-shortcuts
                ''',
                'ldp_sync_igp_shortcuts',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('link-down-fast-detect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable registration for early interface
                down notifications
                ''',
                'link_down_fast_detect',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('loopback-stub-network', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable advertising loopback as a stub
                network
                ''',
                'loopback_stub_network',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('network-type', REFERENCE_ENUM_CLASS, 'OspfNetworkEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfNetworkEnum', 
                [], [], 
                '''                Type of attached network
                ''',
                'network_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-suppression-secondary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable prefix suppression for secondary
                addresses
                ''',
                'prefix_suppression_secondary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Router priority for DR and BDR election
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('security', REFERENCE_CLASS, 'Security' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Security', 
                [], [], 
                '''                Container class for security related
                configuration parameters
                ''',
                'security',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingEnum', 
                [], [], 
                '''                segment-routing configuration Applicable only in
                Default VRF
                ''',
                'segment_routing',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing-forwarding', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingForwardingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingForwardingEnum', 
                [], [], 
                '''                segment-routing forwarding configuration
                Applicableonly in Default VRF
                ''',
                'segment_routing_forwarding',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('srgb', REFERENCE_CLASS, 'Srgb' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Srgb', 
                [], [], 
                '''                Segment Routing Global Block configuration
                ''',
                'srgb',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-in', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable an OSPF area to advertise
                external prefixes into this area as summary
                ''',
                'summary_in',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'process-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.ConnectedOrStaticOrDagrOrSubscriberOrMobileOrRip' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.ConnectedOrStaticOrDagrOrSubscriberOrMobileOrRip',
            False, 
            [
            _MetaInfoClassMember('bgp-preserve-default-info', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve Metric and Metric Type of BGP
                Default Route
                ''',
                'bgp_preserve_default_info',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bgp-preserve-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve MED of BGP routes
                ''',
                'bgp_preserve_med',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('classful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disallow subnetting
                ''',
                'classful',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-redistributed-route-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                Default metric for routes being
                redistributed into OSPF
                ''',
                'default_redistributed_route_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'OspfEigrpRouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfEigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('isis-levels', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                Levels of ISIS routes
                ''',
                'isis_levels',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                Set OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-external', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF external route types
                ''',
                'ospf_external',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-internal', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                OSPF_Internal route type
                ''',
                'ospf_internal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-nssa-level', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF NSSA external route types
                ''',
                'ospf_nssa_level',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-redist-lsa-type', REFERENCE_ENUM_CLASS, 'OspfRedistLsaEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRedistLsaEnum', 
                [], [], 
                '''                LSA type for redistributed routes
                ''',
                'ospf_redist_lsa_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospfnssa-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only redistribute to NSSA areas
                ''',
                'ospfnssa_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Routing policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Set tag for routes redistributed into OSPF
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'connected-or-static-or-dagr-or-subscriber-or-mobile-or-rip',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.ApplicationOrIsisOrOspf' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.ApplicationOrIsisOrOspf',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF or ISIS process name or protocol name:
                bgp, eigrp, connected
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('bgp-preserve-default-info', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve Metric and Metric Type of BGP
                Default Route
                ''',
                'bgp_preserve_default_info',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bgp-preserve-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve MED of BGP routes
                ''',
                'bgp_preserve_med',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('classful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disallow subnetting
                ''',
                'classful',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-redistributed-route-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                Default metric for routes being
                redistributed into OSPF
                ''',
                'default_redistributed_route_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'OspfEigrpRouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfEigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('isis-levels', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                Levels of ISIS routes
                ''',
                'isis_levels',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                Set OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-external', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF external route types
                ''',
                'ospf_external',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-internal', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                OSPF_Internal route type
                ''',
                'ospf_internal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-nssa-level', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF NSSA external route types
                ''',
                'ospf_nssa_level',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-redist-lsa-type', REFERENCE_ENUM_CLASS, 'OspfRedistLsaEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRedistLsaEnum', 
                [], [], 
                '''                LSA type for redistributed routes
                ''',
                'ospf_redist_lsa_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospfnssa-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only redistribute to NSSA areas
                ''',
                'ospfnssa_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Routing policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Set tag for routes redistributed into OSPF
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'application-or-isis-or-ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.Bgp' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.Bgp',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                First half of BGP AS number in XX.YY format.
                Mandatory if Protocol is BGP and must not be
                specified otherwise. Must be a non-zero
                value if second half is zero.
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Second half of BGP AS number in XX.YY format
                . Mandatory if Protocol is BGP or EIGRP and
                must not be specified otherwise. Must be a
                non-zero value if first half is zero.
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF or ISIS process name or protocol name:
                bgp, eigrp, connected
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('bgp-preserve-default-info', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve Metric and Metric Type of BGP
                Default Route
                ''',
                'bgp_preserve_default_info',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bgp-preserve-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve MED of BGP routes
                ''',
                'bgp_preserve_med',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('classful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disallow subnetting
                ''',
                'classful',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-redistributed-route-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                Default metric for routes being
                redistributed into OSPF
                ''',
                'default_redistributed_route_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'OspfEigrpRouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfEigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('isis-levels', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                Levels of ISIS routes
                ''',
                'isis_levels',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                Set OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-external', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF external route types
                ''',
                'ospf_external',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-internal', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                OSPF_Internal route type
                ''',
                'ospf_internal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-nssa-level', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF NSSA external route types
                ''',
                'ospf_nssa_level',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-redist-lsa-type', REFERENCE_ENUM_CLASS, 'OspfRedistLsaEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRedistLsaEnum', 
                [], [], 
                '''                LSA type for redistributed routes
                ''',
                'ospf_redist_lsa_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospfnssa-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only redistribute to NSSA areas
                ''',
                'ospfnssa_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Routing policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Set tag for routes redistributed into OSPF
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.Eigrp' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.Eigrp',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                First half of BGP AS number in XX.YY format.
                Mandatory if Protocol is BGP and must not be
                specified otherwise. Must be a non-zero
                value if second half is zero.
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF or ISIS process name or protocol name:
                bgp, eigrp, connected
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('bgp-preserve-default-info', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve Metric and Metric Type of BGP
                Default Route
                ''',
                'bgp_preserve_default_info',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bgp-preserve-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve MED of BGP routes
                ''',
                'bgp_preserve_med',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('classful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disallow subnetting
                ''',
                'classful',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-redistributed-route-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                Default metric for routes being
                redistributed into OSPF
                ''',
                'default_redistributed_route_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'OspfEigrpRouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfEigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('isis-levels', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                Levels of ISIS routes
                ''',
                'isis_levels',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                Set OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-external', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF external route types
                ''',
                'ospf_external',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-internal', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                OSPF_Internal route type
                ''',
                'ospf_internal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-nssa-level', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF NSSA external route types
                ''',
                'ospf_nssa_level',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-redist-lsa-type', REFERENCE_ENUM_CLASS, 'OspfRedistLsaEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRedistLsaEnum', 
                [], [], 
                '''                LSA type for redistributed routes
                ''',
                'ospf_redist_lsa_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospfnssa-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only redistribute to NSSA areas
                ''',
                'ospfnssa_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Routing policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Set tag for routes redistributed into OSPF
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'eigrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'OspfRedistProtocolEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRedistProtocolEnum', 
                [], [], 
                '''                Distribute list protocol type
                ''',
                'protocol_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('application-or-isis-or-ospf', REFERENCE_LIST, 'ApplicationOrIsisOrOspf' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.ApplicationOrIsisOrOspf', 
                [], [], 
                '''                application or isis or ospf
                ''',
                'application_or_isis_or_ospf',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bgp', REFERENCE_LIST, 'Bgp' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.Bgp', 
                [], [], 
                '''                bgp
                ''',
                'bgp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('connected-or-static-or-dagr-or-subscriber-or-mobile-or-rip', REFERENCE_CLASS, 'ConnectedOrStaticOrDagrOrSubscriberOrMobileOrRip' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.ConnectedOrStaticOrDagrOrSubscriberOrMobileOrRip', 
                [], [], 
                '''                connected or static or dagr or subscriber or
                mobile or rip
                ''',
                'connected_or_static_or_dagr_or_subscriber_or_mobile_or_rip',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('eigrp', REFERENCE_LIST, 'Eigrp' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.Eigrp', 
                [], [], 
                '''                eigrp
                ''',
                'eigrp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'redistribute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes',
            False, 
            [
            _MetaInfoClassMember('redistribute', REFERENCE_LIST, 'Redistribute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute', 
                [], [], 
                '''                Redistribute information from another routing
                protocol
                ''',
                'redistribute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'redistributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Redistribution' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Redistribution',
            False, 
            [
            _MetaInfoClassMember('redistributes', REFERENCE_CLASS, 'Redistributes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes', 
                [], [], 
                '''                Redistribute information from another routing
                protocol
                ''',
                'redistributes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'redistribution',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AdjacencyStagger' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AdjacencyStagger',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable OSPF adjacency stagger
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('initial-nbr', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Adjacency Stagger: Initial number of neighbors
                to bring up per area
                ''',
                'initial_nbr',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-nbr', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Adjacency Stagger: Subsequent simultaneous
                number of neighbors to bring up
                ''',
                'max_nbr',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'adjacency-stagger',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.MaxLsa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.MaxLsa',
            False, 
            [
            _MetaInfoClassMember('max-lsa-ignore-count', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967294)], [], 
                '''                Set count on how many times adjacencies can be
                suppressed
                ''',
                'max_lsa_ignore_count',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-lsa-ignore-time', ATTRIBUTE, 'int' , None, None, 
                [(1, 35791394)], [], 
                '''                Set time during which all adjacencies are
                suppressed
                ''',
                'max_lsa_ignore_time',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-lsa-limit', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967294)], [], 
                '''                Set maximum number of non self-generated LSAs
                ''',
                'max_lsa_limit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-lsa-reset-time', ATTRIBUTE, 'int' , None, None, 
                [(2, 71582788)], [], 
                '''                Set number of minutes after which ignore-count
                is reset to zero
                ''',
                'max_lsa_reset_time',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-lsa-threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Set max-lsa threshold for generating a warning
                message
                ''',
                'max_lsa_threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-lsa-warning-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only give warning message when limit is
                exceeded
                ''',
                'max_lsa_warning_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AutoCost' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AutoCost',
            False, 
            [
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                The reference bandwidth in terms of Mbits per
                second
                ''',
                'bandwidth',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disabling auto costing
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'auto-cost',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Ucmp.Enable' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Ucmp.Enable',
            False, 
            [
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Prefix List
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('variance', ATTRIBUTE, 'int' , None, None, 
                [(101, 10000)], [], 
                '''                Value of variance
                ''',
                'variance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'enable',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Ucmp.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Ucmp.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Ucmp.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Ucmp.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Ucmp.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Ucmp' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Ucmp',
            False, 
            [
            _MetaInfoClassMember('delay-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 5000)], [], 
                '''                Delay in msecs between primary SPF and UCMP
                computation
                ''',
                'delay_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('enable', REFERENCE_CLASS, 'Enable' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Ucmp.Enable', 
                [], [], 
                '''                UCMP feature enable configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Ucmp.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ucmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'OspfFastReroutePriorityEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastReroutePriorityEnum', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix priority-limit
                command
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker',
            False, 
            [
            _MetaInfoClassMember('tiebreaker-type', REFERENCE_ENUM_CLASS, 'OspfFastRerouteTiebreakersEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastRerouteTiebreakersEnum', 
                [], [], 
                '''                Tiebreaker type
                ''',
                'tiebreaker_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('tiebreaker-index', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Index value for a tiebreaker
                ''',
                'tiebreaker_index',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'tiebreaker',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers',
            False, 
            [
            _MetaInfoClassMember('tiebreaker', REFERENCE_LIST, 'Tiebreaker' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker', 
                [], [], 
                '''                Fast-reroute tiebreakers configuration
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'tiebreakers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('load-sharing-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable load sharing between multiple backups
                ''',
                'load_sharing_disable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'OspfFastReroutePriorityEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastReroutePriorityEnum', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix priority-limit
                command
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tiebreakers', REFERENCE_CLASS, 'Tiebreakers' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers', 
                [], [], 
                '''                Fast-reroute tiebreakers configurations
                ''',
                'tiebreakers',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.FastReroute',
            False, 
            [
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link global configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix global configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.SummaryPrefixData' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.SummaryPrefixData',
            False, 
            [
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise when translating OSPF type-7
                LSA
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                32-bit tag value
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'summary-prefix-data',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.PrefixAndNetmask' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.PrefixAndNetmask',
            False, 
            [
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Summary netmask
                ''',
                'netmask',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP summary prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise when translating OSPF type-7
                LSA
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                32-bit tag value
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'prefix-and-netmask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.Prefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.Prefix',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP summary prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise when translating OSPF type-7
                LSA
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                32-bit tag value
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.Netmask' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.Netmask',
            False, 
            [
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Summary netmask
                ''',
                'netmask',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise when translating OSPF type-7
                LSA
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                32-bit tag value
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'netmask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes',
            False, 
            [
            _MetaInfoClassMember('netmask', REFERENCE_LIST, 'Netmask' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.Netmask', 
                [], [], 
                '''                keys: netmask
                ''',
                'netmask',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix', REFERENCE_LIST, 'Prefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.Prefix', 
                [], [], 
                '''                keys: prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-and-netmask', REFERENCE_LIST, 'PrefixAndNetmask' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.PrefixAndNetmask', 
                [], [], 
                '''                keys: prefix, netmask
                ''',
                'prefix_and_netmask',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-prefix-data', REFERENCE_CLASS, 'SummaryPrefixData' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.SummaryPrefixData', 
                [], [], 
                '''                Data container.
                ''',
                'summary_prefix_data',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'summary-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.OutgoingRouteUpdates.OutgoingRouteUpdate' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.OutgoingRouteUpdates.OutgoingRouteUpdate',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'OspfDistListProtocolEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfDistListProtocolEnum', 
                [], [], 
                '''                Distribute list protocol type
                ''',
                'protocol_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                First half of BGP AS number in XX.YY format. 
                Mandatory if Protocol is BGP and must not be
                specified otherwise. Must be a non-zero value
                if second half is zero.
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Second half of BGP AS number in XX.YY format.
                Mandatory if Protocol is BGP and must not be
                specified otherwise. Must be a non-zero value
                if first half is zero.
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF process name
                ''',
                'ospf_process_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'outgoing-route-update',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.OutgoingRouteUpdates' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.OutgoingRouteUpdates',
            False, 
            [
            _MetaInfoClassMember('outgoing-route-update', REFERENCE_LIST, 'OutgoingRouteUpdate' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.OutgoingRouteUpdates.OutgoingRouteUpdate', 
                [], [], 
                '''                Filter outgoing routing updates for a
                particular protocol
                ''',
                'outgoing_route_update',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'outgoing-route-updates',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Distance.OspfDistance' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Distance.OspfDistance',
            False, 
            [
            _MetaInfoClassMember('external-routes', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Distance for external type 5 and type 7 routes
                ''',
                'external_routes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('inter-area', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Distance for inter-area routes
                ''',
                'inter_area',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('intra-area', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Distance for intra-area routes
                ''',
                'intra_area',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ospf-distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Distance.IpDistances.IpDistance' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Distance.IpDistances.IpDistance',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP source address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('wildcard', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP wild card bits -- inverted mask
                ''',
                'wildcard',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ip-distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Distance.IpDistances' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Distance.IpDistances',
            False, 
            [
            _MetaInfoClassMember('ip-distance', REFERENCE_LIST, 'IpDistance' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Distance.IpDistances.IpDistance', 
                [], [], 
                '''                Administrative distance configuration for a
                particular IP address
                ''',
                'ip_distance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ip-distances',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Distance' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Distance',
            False, 
            [
            _MetaInfoClassMember('admin-distance', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Define an administrative distance
                ''',
                'admin_distance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ip-distances', REFERENCE_CLASS, 'IpDistances' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Distance.IpDistances', 
                [], [], 
                '''                IP specific administrative distance
                configuration
                ''',
                'ip_distances',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-distance', REFERENCE_CLASS, 'OspfDistance' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Distance.OspfDistance', 
                [], [], 
                '''                OSPF distance configuration
                ''',
                'ospf_distance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router ID of virtual link neighbor
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'virtual-link-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes',
            False, 
            [
            _MetaInfoClassMember('virtual-link-scope', REFERENCE_LIST, 'VirtualLinkScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope', 
                [], [], 
                '''                Virtual Link configuration
                ''',
                'virtual_link_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'virtual-link-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of the remote sham-link endpoint
                ''',
                'destination_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of the local sham-link endpoint
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of the local sham-link endpoint.
                Enter an IP Address
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'sham-link-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes',
            False, 
            [
            _MetaInfoClassMember('sham-link-scope', REFERENCE_LIST, 'ShamLinkScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope', 
                [], [], 
                '''                Sham Link configuration
                ''',
                'sham_link_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'sham-link-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 50)], [], 
                '''                Detection multiplier for BFD sessions created
                by OSPF
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'BfdEnableModeEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'BfdEnableModeEnum', 
                [], [], 
                '''                 use of Bidirectional Forwarding Detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(3, 30000)], [], 
                '''                Hello interval for BFD sessions created by OSPF
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Security.Ttl' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Security.Ttl',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable TTL security
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hop-count', ATTRIBUTE, 'int' , None, None, 
                [(1, 254)], [], 
                '''                Hop count
                ''',
                'hop_count',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ttl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Security' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Security',
            False, 
            [
            _MetaInfoClassMember('ttl', REFERENCE_CLASS, 'Ttl' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Security.Ttl', 
                [], [], 
                '''                Enabling turns on TTL security
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'security',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('maximum-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Maximum path cost to remote LFA
                ''',
                'maximum_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tunnel', REFERENCE_ENUM_CLASS, 'OspfFrrRlfaTunnelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFrrRlfaTunnelEnum', 
                [], [], 
                '''                Enable/Disable remote LFA computation
                ''',
                'tunnel',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.RemoteLfa', 
                [], [], 
                '''                Remote LFA configuration
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('topology-independent-lfa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Topology Independet LFA configuration
                ''',
                'topology_independent_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'OspfFastRerouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF demand circuit
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-auto-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS LDP Auto Config
                ''',
                'ldp_auto_config',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync-igp-shortcuts', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync for igp-shortcuts
                ''',
                'ldp_sync_igp_shortcuts',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('link-down-fast-detect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable registration for early interface
                down notifications
                ''',
                'link_down_fast_detect',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('loopback-stub-network', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable advertising loopback as a stub
                network
                ''',
                'loopback_stub_network',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('network-type', REFERENCE_ENUM_CLASS, 'OspfNetworkEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfNetworkEnum', 
                [], [], 
                '''                Type of attached network
                ''',
                'network_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-suppression-secondary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable prefix suppression for secondary
                addresses
                ''',
                'prefix_suppression_secondary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Router priority for DR and BDR election
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('security', REFERENCE_CLASS, 'Security' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Security', 
                [], [], 
                '''                Container class for security related
                configuration parameters
                ''',
                'security',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing-forwarding', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingForwardingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingForwardingEnum', 
                [], [], 
                '''                segment-routing forwarding configuration
                Applicableonly in Default VRF
                ''',
                'segment_routing_forwarding',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.PrefixSid' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.PrefixSid',
            False, 
            [
            _MetaInfoClassMember('explicit-null', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Force Penultimate Hop To Send Explicit-Null
                Label
                ''',
                'explicit_null',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('sid-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 1048575)], [], 
                '''                SID value
                ''',
                'sid_value',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'OspfSidEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSidEnum', 
                [], [], 
                '''                OSPF SID Type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'prefix-sid',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 50)], [], 
                '''                Detection multiplier for BFD sessions created
                by OSPF
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'BfdEnableModeEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'BfdEnableModeEnum', 
                [], [], 
                '''                 use of Bidirectional Forwarding Detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(3, 30000)], [], 
                '''                Hello interval for BFD sessions created by OSPF
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security.Ttl' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security.Ttl',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable TTL security
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hop-count', ATTRIBUTE, 'int' , None, None, 
                [(1, 254)], [], 
                '''                Hop count
                ''',
                'hop_count',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ttl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security',
            False, 
            [
            _MetaInfoClassMember('ttl', REFERENCE_CLASS, 'Ttl' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security.Ttl', 
                [], [], 
                '''                Enabling turns on TTL security
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'security',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('maximum-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Maximum path cost to remote LFA
                ''',
                'maximum_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tunnel', REFERENCE_ENUM_CLASS, 'OspfFrrRlfaTunnelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFrrRlfaTunnelEnum', 
                [], [], 
                '''                Enable/Disable remote LFA computation
                ''',
                'tunnel',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa', 
                [], [], 
                '''                Remote LFA configuration
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('topology-independent-lfa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Topology Independet LFA configuration
                ''',
                'topology_independent_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'OspfFastRerouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                OSPF cost for point-to-multipoint neighbor
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Database filter: Filter OSPF LSA during
                synchronization and flooding for
                point-to-multipoint
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                OSPF dead router poll-interval in seconds
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                OSPF priority of non-broadcast neighbor
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors.Neighbor', 
                [], [], 
                '''                Router configuration information for a
                particular neighbor
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF demand circuit
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-auto-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS LDP Auto Config
                ''',
                'ldp_auto_config',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync-igp-shortcuts', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync for igp-shortcuts
                ''',
                'ldp_sync_igp_shortcuts',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('link-down-fast-detect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable registration for early interface
                down notifications
                ''',
                'link_down_fast_detect',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('loopback-stub-network', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable advertising loopback as a stub
                network
                ''',
                'loopback_stub_network',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors', 
                [], [], 
                '''                Neighbor router configuration information
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('network-type', REFERENCE_ENUM_CLASS, 'OspfNetworkEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfNetworkEnum', 
                [], [], 
                '''                Type of attached network
                ''',
                'network_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-sid', REFERENCE_CLASS, 'PrefixSid' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.PrefixSid', 
                [], [], 
                '''                Prefix SID
                ''',
                'prefix_sid',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-suppression-secondary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable prefix suppression for secondary
                addresses
                ''',
                'prefix_suppression_secondary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Router priority for DR and BDR election
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('security', REFERENCE_CLASS, 'Security' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security', 
                [], [], 
                '''                Container class for security related
                configuration parameters
                ''',
                'security',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing-forwarding', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingForwardingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingForwardingEnum', 
                [], [], 
                '''                segment-routing forwarding configuration
                Applicableonly in Default VRF
                ''',
                'segment_routing_forwarding',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'name-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes',
            False, 
            [
            _MetaInfoClassMember('name-scope', REFERENCE_LIST, 'NameScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope', 
                [], [], 
                '''                Name scope configuration
                ''',
                'name_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'name-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                OSPF cost for point-to-multipoint neighbor
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Database filter: Filter OSPF LSA during
                synchronization and flooding for
                point-to-multipoint
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                OSPF dead router poll-interval in seconds
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                OSPF priority of non-broadcast neighbor
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor', 
                [], [], 
                '''                Router configuration information for a
                particular neighbor
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of Multi Area Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors', 
                [], [], 
                '''                Neighbor router configuration information
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'multi-area-interface-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes',
            False, 
            [
            _MetaInfoClassMember('multi-area-interface-scope', REFERENCE_LIST, 'MultiAreaInterfaceScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope', 
                [], [], 
                '''                Multi Area Interface configuration
                ''',
                'multi_area_interface_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'multi-area-interface-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaRanges.AreaRange' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaRanges.AreaRange',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address to match
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP netmask for address
                ''',
                'netmask',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise this range
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-range',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaRanges' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaRanges',
            False, 
            [
            _MetaInfoClassMember('area-range', REFERENCE_LIST, 'AreaRange' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaRanges.AreaRange', 
                [], [], 
                '''                Ordering index
                ''',
                'area_range',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Nssa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Nssa',
            False, 
            [
            _MetaInfoClassMember('default-info-originate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Originate Type 7 default into NSSA area
                ''',
                'default_info_originate',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('no-redistribution', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                No redistribution into this NSSA area
                ''',
                'no_redistribution',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('no-summary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not send summary LSA into NSSA
                ''',
                'no_summary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('nssa-def-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                OSPF default metric
                ''',
                'nssa_def_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'nssa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Area ID if in IP address format
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('area-ranges', REFERENCE_CLASS, 'AreaRanges' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaRanges', 
                [], [], 
                '''                Summarize routes matching address/mask (border
                routers only)
                ''',
                'area_ranges',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('area-scope', REFERENCE_CLASS, 'AreaScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope', 
                [], [], 
                '''                Area scope configuration
                ''',
                'area_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Set the summary default-cost of a NSSA/stub
                area
                ''',
                'default_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable an OSPF area to advertise
                intra-area prefixes out of this area as external
                ''',
                'external_out',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mpls-traffic-eng', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure an OSPF area to run MPLS Traffic
                Engineering
                ''',
                'mpls_traffic_eng',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multi-area-interface-scopes', REFERENCE_CLASS, 'MultiAreaInterfaceScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes', 
                [], [], 
                '''                Multi Area Interface scope configurations
                ''',
                'multi_area_interface_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('name-scopes', REFERENCE_CLASS, 'NameScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes', 
                [], [], 
                '''                Name scope configurations
                ''',
                'name_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('nssa', REFERENCE_CLASS, 'Nssa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Nssa', 
                [], [], 
                '''                Specify area as a NSSA area
                ''',
                'nssa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure a route policy for inbound type-3
                lsa filtering
                ''',
                'route_policy_in',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure a route policy for outbound type-3
                lsa filtering
                ''',
                'route_policy_out',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingEnum', 
                [], [], 
                '''                segment-routing configuration Applicable only in
                Default VRF
                ''',
                'segment_routing',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('sham-link-scopes', REFERENCE_CLASS, 'ShamLinkScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes', 
                [], [], 
                '''                Sham Link scope configurations
                ''',
                'sham_link_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify the area as a stub area (send summary
                LSA stub area)
                ''',
                'stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-in', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable an OSPF area to advertise
                external prefixes into this area as summary
                ''',
                'summary_in',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-link-scopes', REFERENCE_CLASS, 'VirtualLinkScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes', 
                [], [], 
                '''                Virtual Link scope configurations
                ''',
                'virtual_link_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router ID of virtual link neighbor
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'virtual-link-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes',
            False, 
            [
            _MetaInfoClassMember('virtual-link-scope', REFERENCE_LIST, 'VirtualLinkScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope', 
                [], [], 
                '''                Virtual Link configuration
                ''',
                'virtual_link_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'virtual-link-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of the remote sham-link endpoint
                ''',
                'destination_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of the local sham-link endpoint
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of the local sham-link endpoint.
                Enter an IP Address
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'sham-link-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes',
            False, 
            [
            _MetaInfoClassMember('sham-link-scope', REFERENCE_LIST, 'ShamLinkScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope', 
                [], [], 
                '''                Sham Link configuration
                ''',
                'sham_link_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'sham-link-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 50)], [], 
                '''                Detection multiplier for BFD sessions created
                by OSPF
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'BfdEnableModeEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'BfdEnableModeEnum', 
                [], [], 
                '''                 use of Bidirectional Forwarding Detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(3, 30000)], [], 
                '''                Hello interval for BFD sessions created by OSPF
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Security.Ttl' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Security.Ttl',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable TTL security
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hop-count', ATTRIBUTE, 'int' , None, None, 
                [(1, 254)], [], 
                '''                Hop count
                ''',
                'hop_count',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ttl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Security' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Security',
            False, 
            [
            _MetaInfoClassMember('ttl', REFERENCE_CLASS, 'Ttl' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Security.Ttl', 
                [], [], 
                '''                Enabling turns on TTL security
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'security',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('maximum-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Maximum path cost to remote LFA
                ''',
                'maximum_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tunnel', REFERENCE_ENUM_CLASS, 'OspfFrrRlfaTunnelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFrrRlfaTunnelEnum', 
                [], [], 
                '''                Enable/Disable remote LFA computation
                ''',
                'tunnel',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.RemoteLfa', 
                [], [], 
                '''                Remote LFA configuration
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('topology-independent-lfa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Topology Independet LFA configuration
                ''',
                'topology_independent_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'OspfFastRerouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF demand circuit
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-auto-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS LDP Auto Config
                ''',
                'ldp_auto_config',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync-igp-shortcuts', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync for igp-shortcuts
                ''',
                'ldp_sync_igp_shortcuts',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('link-down-fast-detect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable registration for early interface
                down notifications
                ''',
                'link_down_fast_detect',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('loopback-stub-network', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable advertising loopback as a stub
                network
                ''',
                'loopback_stub_network',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('network-type', REFERENCE_ENUM_CLASS, 'OspfNetworkEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfNetworkEnum', 
                [], [], 
                '''                Type of attached network
                ''',
                'network_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-suppression-secondary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable prefix suppression for secondary
                addresses
                ''',
                'prefix_suppression_secondary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Router priority for DR and BDR election
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('security', REFERENCE_CLASS, 'Security' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Security', 
                [], [], 
                '''                Container class for security related
                configuration parameters
                ''',
                'security',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing-forwarding', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingForwardingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingForwardingEnum', 
                [], [], 
                '''                segment-routing forwarding configuration
                Applicableonly in Default VRF
                ''',
                'segment_routing_forwarding',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.PrefixSid' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.PrefixSid',
            False, 
            [
            _MetaInfoClassMember('explicit-null', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Force Penultimate Hop To Send Explicit-Null
                Label
                ''',
                'explicit_null',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('sid-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 1048575)], [], 
                '''                SID value
                ''',
                'sid_value',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'OspfSidEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSidEnum', 
                [], [], 
                '''                OSPF SID Type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'prefix-sid',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 50)], [], 
                '''                Detection multiplier for BFD sessions created
                by OSPF
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'BfdEnableModeEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'BfdEnableModeEnum', 
                [], [], 
                '''                 use of Bidirectional Forwarding Detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(3, 30000)], [], 
                '''                Hello interval for BFD sessions created by OSPF
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security.Ttl' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security.Ttl',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable TTL security
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hop-count', ATTRIBUTE, 'int' , None, None, 
                [(1, 254)], [], 
                '''                Hop count
                ''',
                'hop_count',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ttl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security',
            False, 
            [
            _MetaInfoClassMember('ttl', REFERENCE_CLASS, 'Ttl' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security.Ttl', 
                [], [], 
                '''                Enabling turns on TTL security
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'security',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('maximum-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Maximum path cost to remote LFA
                ''',
                'maximum_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tunnel', REFERENCE_ENUM_CLASS, 'OspfFrrRlfaTunnelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFrrRlfaTunnelEnum', 
                [], [], 
                '''                Enable/Disable remote LFA computation
                ''',
                'tunnel',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa', 
                [], [], 
                '''                Remote LFA configuration
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('topology-independent-lfa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Topology Independet LFA configuration
                ''',
                'topology_independent_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'OspfFastRerouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                OSPF cost for point-to-multipoint neighbor
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Database filter: Filter OSPF LSA during
                synchronization and flooding for
                point-to-multipoint
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                OSPF dead router poll-interval in seconds
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                OSPF priority of non-broadcast neighbor
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors.Neighbor', 
                [], [], 
                '''                Router configuration information for a
                particular neighbor
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF demand circuit
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-auto-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS LDP Auto Config
                ''',
                'ldp_auto_config',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync-igp-shortcuts', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync for igp-shortcuts
                ''',
                'ldp_sync_igp_shortcuts',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('link-down-fast-detect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable registration for early interface
                down notifications
                ''',
                'link_down_fast_detect',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('loopback-stub-network', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable advertising loopback as a stub
                network
                ''',
                'loopback_stub_network',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors', 
                [], [], 
                '''                Neighbor router configuration information
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('network-type', REFERENCE_ENUM_CLASS, 'OspfNetworkEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfNetworkEnum', 
                [], [], 
                '''                Type of attached network
                ''',
                'network_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-sid', REFERENCE_CLASS, 'PrefixSid' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.PrefixSid', 
                [], [], 
                '''                Prefix SID
                ''',
                'prefix_sid',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-suppression-secondary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable prefix suppression for secondary
                addresses
                ''',
                'prefix_suppression_secondary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Router priority for DR and BDR election
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('security', REFERENCE_CLASS, 'Security' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security', 
                [], [], 
                '''                Container class for security related
                configuration parameters
                ''',
                'security',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing-forwarding', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingForwardingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingForwardingEnum', 
                [], [], 
                '''                segment-routing forwarding configuration
                Applicableonly in Default VRF
                ''',
                'segment_routing_forwarding',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'name-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes',
            False, 
            [
            _MetaInfoClassMember('name-scope', REFERENCE_LIST, 'NameScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope', 
                [], [], 
                '''                Name scope configuration
                ''',
                'name_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'name-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                OSPF cost for point-to-multipoint neighbor
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Database filter: Filter OSPF LSA during
                synchronization and flooding for
                point-to-multipoint
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                OSPF dead router poll-interval in seconds
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                OSPF priority of non-broadcast neighbor
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor', 
                [], [], 
                '''                Router configuration information for a
                particular neighbor
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of Multi Area Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors', 
                [], [], 
                '''                Neighbor router configuration information
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'multi-area-interface-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes',
            False, 
            [
            _MetaInfoClassMember('multi-area-interface-scope', REFERENCE_LIST, 'MultiAreaInterfaceScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope', 
                [], [], 
                '''                Multi Area Interface configuration
                ''',
                'multi_area_interface_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'multi-area-interface-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaRanges.AreaRange' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaRanges.AreaRange',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address to match
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP netmask for address
                ''',
                'netmask',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise this range
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-range',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaRanges' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaRanges',
            False, 
            [
            _MetaInfoClassMember('area-range', REFERENCE_LIST, 'AreaRange' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaRanges.AreaRange', 
                [], [], 
                '''                Ordering index
                ''',
                'area_range',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Nssa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Nssa',
            False, 
            [
            _MetaInfoClassMember('default-info-originate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Originate Type 7 default into NSSA area
                ''',
                'default_info_originate',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('no-redistribution', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                No redistribution into this NSSA area
                ''',
                'no_redistribution',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('no-summary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not send summary LSA into NSSA
                ''',
                'no_summary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('nssa-def-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                OSPF default metric
                ''',
                'nssa_def_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'nssa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId',
            False, 
            [
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Area ID if in integer format
                ''',
                'area_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('area-ranges', REFERENCE_CLASS, 'AreaRanges' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaRanges', 
                [], [], 
                '''                Summarize routes matching address/mask (border
                routers only)
                ''',
                'area_ranges',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('area-scope', REFERENCE_CLASS, 'AreaScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope', 
                [], [], 
                '''                Area scope configuration
                ''',
                'area_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Set the summary default-cost of a NSSA/stub
                area
                ''',
                'default_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable an OSPF area to advertise
                intra-area prefixes out of this area as external
                ''',
                'external_out',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mpls-traffic-eng', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure an OSPF area to run MPLS Traffic
                Engineering
                ''',
                'mpls_traffic_eng',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multi-area-interface-scopes', REFERENCE_CLASS, 'MultiAreaInterfaceScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes', 
                [], [], 
                '''                Multi Area Interface scope configurations
                ''',
                'multi_area_interface_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('name-scopes', REFERENCE_CLASS, 'NameScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes', 
                [], [], 
                '''                Name scope configurations
                ''',
                'name_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('nssa', REFERENCE_CLASS, 'Nssa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Nssa', 
                [], [], 
                '''                Specify area as a NSSA area
                ''',
                'nssa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure a route policy for inbound type-3
                lsa filtering
                ''',
                'route_policy_in',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure a route policy for outbound type-3
                lsa filtering
                ''',
                'route_policy_out',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingEnum', 
                [], [], 
                '''                segment-routing configuration Applicable only in
                Default VRF
                ''',
                'segment_routing',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('sham-link-scopes', REFERENCE_CLASS, 'ShamLinkScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes', 
                [], [], 
                '''                Sham Link scope configurations
                ''',
                'sham_link_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify the area as a stub area (send summary
                LSA stub area)
                ''',
                'stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-in', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable an OSPF area to advertise
                external prefixes into this area as summary
                ''',
                'summary_in',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-link-scopes', REFERENCE_CLASS, 'VirtualLinkScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes', 
                [], [], 
                '''                Virtual Link scope configurations
                ''',
                'virtual_link_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-area-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses',
            False, 
            [
            _MetaInfoClassMember('area-address', REFERENCE_LIST, 'AreaAddress' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress', 
                [], [], 
                '''                Configuration for a particular area
                ''',
                'area_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('area-area-id', REFERENCE_LIST, 'AreaAreaId' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId', 
                [], [], 
                '''                Configuration for a particular area
                ''',
                'area_area_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Timers.SpfTimer' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Timers.SpfTimer',
            False, 
            [
            _MetaInfoClassMember('backoff-increment', ATTRIBUTE, 'int' , None, None, 
                [(1, 600000)], [], 
                '''                Number of milliseconds delay between
                successive SPF runs
                ''',
                'backoff_increment',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('initial-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 600000)], [], 
                '''                Number of milliseconds before first SPF run
                ''',
                'initial_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 600000)], [], 
                '''                Max number of milliseconds between consecutive
                SPF calculations
                ''',
                'max_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'spf-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Timers.LsaGenerationTimer' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Timers.LsaGenerationTimer',
            False, 
            [
            _MetaInfoClassMember('backoff-increment', ATTRIBUTE, 'int' , None, None, 
                [(1, 600000)], [], 
                '''                Number of milliseconds delay between
                successive LSA builds
                ''',
                'backoff_increment',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('initial-delay', ATTRIBUTE, 'int' , None, None, 
                [(0, 600000)], [], 
                '''                Number of milliseconds before generating first
                LSA
                ''',
                'initial_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 600000)], [], 
                '''                Max number of milliseconds between consecutive
                LSA builds 
                ''',
                'max_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'lsa-generation-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf.Timers' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf.Timers',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-timer', ATTRIBUTE, 'int' , None, None, 
                [(50, 600000)], [], 
                '''                Number of ms between end of SPF and start of
                IPFRR computation
                ''',
                'fast_reroute_timer',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lsa-generation-timer', REFERENCE_CLASS, 'LsaGenerationTimer' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Timers.LsaGenerationTimer', 
                [], [], 
                '''                OSPF LSA timers (in milliseconds)
                ''',
                'lsa_generation_timer',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lsa-group-pacing', ATTRIBUTE, 'int' , None, None, 
                [(10, 1800)], [], 
                '''                LSA group pacing timer (Seconds between group
                of LSAs being refreshed or maxaged)
                ''',
                'lsa_group_pacing',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lsa-min-arrival', ATTRIBUTE, 'int' , None, None, 
                [(0, 600000)], [], 
                '''                MinLSArrival timer (minimum interval in
                milliseconds between accepting the same LSA)
                ''',
                'lsa_min_arrival',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lsa-pacing-flood', ATTRIBUTE, 'int' , None, None, 
                [(5, 100)], [], 
                '''                Seconds between group of LSAs being refreshed
                or maxaged
                ''',
                'lsa_pacing_flood',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lsa-refresh', ATTRIBUTE, 'int' , None, None, 
                [(1800, 2700)], [], 
                '''                How often self-originated LSAs should be
                refreshed
                ''',
                'lsa_refresh',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('spf-timer', REFERENCE_CLASS, 'SpfTimer' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Timers.SpfTimer', 
                [], [], 
                '''                OSPF SPF timers (in milliseconds)
                ''',
                'spf_timer',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name for this vrf
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('adjacency-changes', REFERENCE_ENUM_CLASS, 'OspfLogAdjEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLogAdjEnum', 
                [], [], 
                '''                Log changes in adjacency state
                ''',
                'adjacency_changes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('adjacency-stagger', REFERENCE_CLASS, 'AdjacencyStagger' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AdjacencyStagger', 
                [], [], 
                '''                Staggering OSPF adjacency bring up
                ''',
                'adjacency_stagger',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('af', REFERENCE_CLASS, 'Af' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Af', 
                [], [], 
                '''                OSPF address family
                ''',
                'af',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('area-addresses', REFERENCE_CLASS, 'AreaAddresses' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses', 
                [], [], 
                '''                Area configuration
                ''',
                'area_addresses',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('auto-cost', REFERENCE_CLASS, 'AutoCost' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.AutoCost', 
                [], [], 
                '''                Controls automatic cost based on bandwidth
                ''',
                'auto_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-information', REFERENCE_CLASS, 'DefaultInformation' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.DefaultInformation', 
                [], [], 
                '''                Control distribution of default information
                ''',
                'default_information',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                Set default metric of redistributed routes
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('disable-dn-bit-check', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable DN bit check
                ''',
                'disable_dn_bit_check',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distance', REFERENCE_CLASS, 'Distance' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Distance', 
                [], [], 
                '''                Administrative distance configuration
                ''',
                'distance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('domain-id', REFERENCE_CLASS, 'DomainId' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.DomainId', 
                [], [], 
                '''                OSPF Domain ID
                ''',
                'domain_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('domain-tag', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                32 bit Domain tag value
                ''',
                'domain_tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.FastReroute', 
                [], [], 
                '''                Fast-reroute instance scoped parameters
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ignore-mospf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Ignore MOSPF (Type 6) LSAs
                ''',
                'ignore_mospf',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-lsa', REFERENCE_CLASS, 'MaxLsa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.MaxLsa', 
                [], [], 
                '''                Set max-lsa configuration
                ''',
                'max_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-metric', REFERENCE_CLASS, 'MaxMetric' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.MaxMetric', 
                [], [], 
                '''                Set maximum metric configuration
                ''',
                'max_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('maximum-interfaces', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Max number of interfaces allowed to be
                configured
                ''',
                'maximum_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [(1, 64)], [], 
                '''                Forward packets over multiple paths (number of
                paths)
                ''',
                'maximum_paths',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('maximum-redistribute-prefix', REFERENCE_CLASS, 'MaximumRedistributePrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.MaximumRedistributePrefix', 
                [], [], 
                '''                Maximum number of prefixes redistributed into
                OSPF
                ''',
                'maximum_redistribute_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('microloop', REFERENCE_CLASS, 'Microloop' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Microloop', 
                [], [], 
                '''                Microloop configuration
                ''',
                'microloop',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('no-opaque', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable opaque LSAs
                ''',
                'no_opaque',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('nsf', REFERENCE_CLASS, 'Nsf' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Nsf', 
                [], [], 
                '''                Non Stop Forwarding configuration
                ''',
                'nsf',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('outgoing-route-updates', REFERENCE_CLASS, 'OutgoingRouteUpdates' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.OutgoingRouteUpdates', 
                [], [], 
                '''                Filter outgoing routing updates
                ''',
                'outgoing_route_updates',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('process-scope', REFERENCE_CLASS, 'ProcessScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.ProcessScope', 
                [], [], 
                '''                Process scope configuration
                ''',
                'process_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Queue', 
                [], [], 
                '''                Adjust OSPF input queue sizes and processing
                quantums
                ''',
                'queue',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('redistribution', REFERENCE_CLASS, 'Redistribution' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Redistribution', 
                [], [], 
                '''                Redistribute configurations
                ''',
                'redistribution',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router ID for this OSPF process. Enter an IP
                Address.
                ''',
                'router_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('snmp-context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF SNMP context configuration
                ''',
                'snmp_context',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('snmp-trap-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable OSPF SNMP trap
                ''',
                'snmp_trap_enabled',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('spf-prefix-priority', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure a route-policy for prioritizing RIB
                route install.
                ''',
                'spf_prefix_priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-prefixes', REFERENCE_CLASS, 'SummaryPrefixes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes', 
                [], [], 
                '''                Configure IP prefix summary
                ''',
                'summary_prefixes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Timers', 
                [], [], 
                '''                Adjust routing timers
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type7', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Prefer type7 externals over type5
                ''',
                'type7',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ucmp', REFERENCE_CLASS, 'Ucmp' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf.Ucmp', 
                [], [], 
                '''                Unequal Cost Multi-ptah configuration
                ''',
                'ucmp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('vrf-lite', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                VRF lite capability
                ''',
                'vrf_lite',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('vrf-start', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Start OSPF VRF configuration
                ''',
                'vrf_start',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs.Vrf', 
                [], [], 
                '''                Configuration for a particular OSPF vrf
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.MonitorConvergence' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.MonitorConvergence',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable convergence monitoring
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enable the monitoring of individual prefixes
                (prefix list name)
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('track-external-routes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the monitoring of External routes
                ''',
                'track_external_routes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('track-ip-frr', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the Tracking of IP-Frr Convergence
                ''',
                'track_ip_frr',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('track-summary-routes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the monitoring of Summary routes
                ''',
                'track_summary_routes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'monitor-convergence',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.SegmentRouting.SrPrefer' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.SegmentRouting.SrPrefer',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable SR labels to be preferred over LDP
                labels
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Prefix List
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'sr-prefer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.SegmentRouting' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.SegmentRouting',
            False, 
            [
            _MetaInfoClassMember('prefix-sid-map-advertise-local', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable advertisement of local SRMS entries
                ''',
                'prefix_sid_map_advertise_local',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-sid-map-receive-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable prefix-SID mapping client
                ''',
                'prefix_sid_map_receive_disable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('sr-prefer', REFERENCE_CLASS, 'SrPrefer' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.SegmentRouting.SrPrefer', 
                [], [], 
                '''                Prefer segment routing labels over LDP
                labels
                ''',
                'sr_prefer',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'segment-routing',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Mpls.MplsRouterId' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Mpls.MplsRouterId',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                MPLS-TE stable IP address for this OSPF
                process
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                MPLS-TE stable loopback interface for this
                OSPF process
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'mpls-router-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Mpls' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Mpls',
            False, 
            [
            _MetaInfoClassMember('autoroute-exclude', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exclude IP destinations from using TE
                tunnels
                ''',
                'autoroute_exclude',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('igp-intact', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable igp-intact mode in OSPF
                ''',
                'igp_intact',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync-update', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable LDP sync induced metric propagation
                ''',
                'ldp_sync_update',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mpls-router-id', REFERENCE_CLASS, 'MplsRouterId' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Mpls.MplsRouterId', 
                [], [], 
                '''                MPLS-TE stable loopback address for this
                OSPF process.Enter either as IP Address or
                Interface name, but not both. Unused field
                must be nil
                ''',
                'mpls_router_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multicast-intact', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable multicast-intact mode in OSPF
                ''',
                'multicast_intact',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Microloop.Avoidance' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Microloop.Avoidance',
            False, 
            [
            _MetaInfoClassMember('enable', REFERENCE_ENUM_CLASS, 'OspfUloopAvoidanceEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfUloopAvoidanceEnum', 
                [], [], 
                '''                MicroLoop avoidance feature enable
                configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('rib-update-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 600000)], [], 
                '''                Delay to introduce between SPF and RIB update
                in msecs
                ''',
                'rib_update_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'avoidance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Microloop' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Microloop',
            False, 
            [
            _MetaInfoClassMember('avoidance', REFERENCE_CLASS, 'Avoidance' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Microloop.Avoidance', 
                [], [], 
                '''                Microloop avoidance configuration
                ''',
                'avoidance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'microloop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.MaximumRedistributePrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.MaximumRedistributePrefix',
            False, 
            [
            _MetaInfoClassMember('number-of-prefixes', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Maximum number of prefixes redistributed
                ''',
                'number_of_prefixes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Threshold value (%) at which to generate a
                warning msg
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('warning-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only give warning messsage when limit is
                exceeded
                ''',
                'warning_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'maximum-redistribute-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.DefaultInformation' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.DefaultInformation',
            False, 
            [
            _MetaInfoClassMember('always-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Always advertise default route
                ''',
                'always_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                OSPF metric
                ''',
                'metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Routing policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'default-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Af' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'OspfAddressFamilyEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'OspfSubAddressFamilyEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSubAddressFamilyEnum', 
                [], [], 
                '''                Sub-Address family
                ''',
                'saf_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Queue' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Queue',
            False, 
            [
            _MetaInfoClassMember('dispatch-incoming', ATTRIBUTE, 'int' , None, None, 
                [(30, 3000)], [], 
                '''                Maximum number of continuous incoming
                packet-related events processed
                ''',
                'dispatch_incoming',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dispatch-rate-limited', ATTRIBUTE, 'int' , None, None, 
                [(30, 3000)], [], 
                '''                Maximum number of continuous rate-limited LSAs
                processed
                ''',
                'dispatch_rate_limited',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dispatch-rate-limited-flush', ATTRIBUTE, 'int' , None, None, 
                [(30, 3000)], [], 
                '''                Maximum number of continuous rate-limited LSAs
                processed for FLUSH
                ''',
                'dispatch_rate_limited_flush',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dispatch-spf-lsa-limit', ATTRIBUTE, 'int' , None, None, 
                [(30, 3000)], [], 
                '''                Maximum number of continuous summary or
                external LSAs processed
                ''',
                'dispatch_spf_lsa_limit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('limit-high', ATTRIBUTE, 'int' , None, None, 
                [(1000, 30000)], [], 
                '''                Hello events are dropped when incoming event
                queue exceeds this
                ''',
                'limit_high',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('limit-low', ATTRIBUTE, 'int' , None, None, 
                [(1000, 30000)], [], 
                '''                DBDs/Updates are dropped when incoming event
                queue exceeds this
                ''',
                'limit_low',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('limit-medium', ATTRIBUTE, 'int' , None, None, 
                [(1000, 30000)], [], 
                '''                LSA ACKs are dropped when incoming event queue
                exceeds this
                ''',
                'limit_medium',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'queue',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnProcRestart' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnProcRestart',
            False, 
            [
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override external-lsa metric with max-metric
                value
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in external-LSAs (default
                16711680)
                ''',
                'external_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set maximum metric for stub links in
                router-LSAs
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('startup-max', ATTRIBUTE, 'int' , None, None, 
                [(5, 86400)], [], 
                '''                Time in seconds to originate router-LSA with
                max-metric
                ''',
                'startup_max',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override summary-lsa metric with max-metric
                value
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in summary-LSAs (default
                16711680)
                ''',
                'summary_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Let BGP decide when to originate router-LSA
                with normal metric
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-metric-on-proc-restart',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnStartup' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnStartup',
            False, 
            [
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override external-lsa metric with max-metric
                value
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in external-LSAs (default
                16711680)
                ''',
                'external_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set maximum metric for stub links in
                router-LSAs
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('startup-max', ATTRIBUTE, 'int' , None, None, 
                [(5, 86400)], [], 
                '''                Time in seconds to originate router-LSA with
                max-metric
                ''',
                'startup_max',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override summary-lsa metric with max-metric
                value
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in summary-LSAs (default
                16711680)
                ''',
                'summary_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Let BGP decide when to originate router-LSA
                with normal metric
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-metric-on-startup',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnProcMigration' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnProcMigration',
            False, 
            [
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override external-lsa metric with max-metric
                value
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in external-LSAs (default
                16711680)
                ''',
                'external_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set maximum metric for stub links in
                router-LSAs
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('startup-max', ATTRIBUTE, 'int' , None, None, 
                [(5, 86400)], [], 
                '''                Time in seconds to originate router-LSA with
                max-metric
                ''',
                'startup_max',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override summary-lsa metric with max-metric
                value
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in summary-LSAs (default
                16711680)
                ''',
                'summary_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Let BGP decide when to originate router-LSA
                with normal metric
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-metric-on-proc-migration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricAlways' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricAlways',
            False, 
            [
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override external-lsa metric with max-metric
                value
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in external-LSAs (default
                16711680)
                ''',
                'external_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set maximum metric for stub links in
                router-LSAs
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override summary-lsa metric with max-metric
                value
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in summary-LSAs (default
                16711680)
                ''',
                'summary_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-metric-always',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnSwitchover' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnSwitchover',
            False, 
            [
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override external-lsa metric with max-metric
                value
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in external-LSAs (default
                16711680)
                ''',
                'external_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set maximum metric for stub links in
                router-LSAs
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('startup-max', ATTRIBUTE, 'int' , None, None, 
                [(5, 86400)], [], 
                '''                Time in seconds to originate router-LSA with
                max-metric
                ''',
                'startup_max',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override summary-lsa metric with max-metric
                value
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-lsa-maximum-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Overriding metric in summary-LSAs (default
                16711680)
                ''',
                'summary_lsa_maximum_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Let BGP decide when to originate router-LSA
                with normal metric
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-metric-on-switchover',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.MaxMetric' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.MaxMetric',
            False, 
            [
            _MetaInfoClassMember('max-metric-always', REFERENCE_CLASS, 'MaxMetricAlways' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricAlways', 
                [], [], 
                '''                Set maximum metric always configuration
                ''',
                'max_metric_always',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-metric-no-abr-off', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Block ABR-disable mode entry while in
                max-metric mode
                ''',
                'max_metric_no_abr_off',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-metric-on-proc-migration', REFERENCE_CLASS, 'MaxMetricOnProcMigration' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnProcMigration', 
                [], [], 
                '''                Set maximum metric on-proc-migration
                configuration
                ''',
                'max_metric_on_proc_migration',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-metric-on-proc-restart', REFERENCE_CLASS, 'MaxMetricOnProcRestart' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnProcRestart', 
                [], [], 
                '''                Set maximum metric on-proc-restart
                configuration
                ''',
                'max_metric_on_proc_restart',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-metric-on-startup', REFERENCE_CLASS, 'MaxMetricOnStartup' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnStartup', 
                [], [], 
                '''                Set maximum metric on-startup configuration
                ''',
                'max_metric_on_startup',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-metric-on-switchover', REFERENCE_CLASS, 'MaxMetricOnSwitchover' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnSwitchover', 
                [], [], 
                '''                Set maximum metric on-switchover configuration
                ''',
                'max_metric_on_switchover',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-metric',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Nsf' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Nsf',
            False, 
            [
            _MetaInfoClassMember('cisco', REFERENCE_ENUM_CLASS, 'OspfCiscoNsfEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfCiscoNsfEnum', 
                [], [], 
                '''                Enable Cisco Non Stop Forwarding
                ''',
                'cisco',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('flush-delay-time', ATTRIBUTE, 'int' , None, None, 
                [(1, 3600)], [], 
                '''                Maximum time allowed for external route
                learning (seconds)
                ''',
                'flush_delay_time',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ietf', REFERENCE_ENUM_CLASS, 'OspfIetfNsfEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfIetfNsfEnum', 
                [], [], 
                '''                Enable IETF Non Stop Forwarding
                ''',
                'ietf',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ietf-strict-lsa-checking', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Strict LSA checking of IETF NSF
                ''',
                'ietf_strict_lsa_checking',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ietf-support-role', REFERENCE_ENUM_CLASS, 'OspfIetfNsfSupportEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfIetfNsfSupportEnum', 
                [], [], 
                '''                Disable helper support role for IETF Non Stop
                Forwarding
                ''',
                'ietf_support_role',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(90, 3600)], [], 
                '''                Minimum interval between Non Stop Forwarding
                restarts in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [(90, 1800)], [], 
                '''                Maximum route lifetime following restart in
                seconds
                ''',
                'lifetime',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'nsf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.Srgb' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.Srgb',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int' , None, None, 
                [(16000, 1048575)], [], 
                '''                The lower bound of the SRGB
                ''',
                'lower_bound',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int' , None, None, 
                [(16000, 1048575)], [], 
                '''                The upper bound of the SRGB
                ''',
                'upper_bound',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'srgb',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 50)], [], 
                '''                Detection multiplier for BFD sessions created
                by OSPF
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'BfdEnableModeEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'BfdEnableModeEnum', 
                [], [], 
                '''                 use of Bidirectional Forwarding Detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(3, 30000)], [], 
                '''                Hello interval for BFD sessions created by OSPF
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.Security.Ttl' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.Security.Ttl',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable TTL security
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hop-count', ATTRIBUTE, 'int' , None, None, 
                [(1, 254)], [], 
                '''                Hop count
                ''',
                'hop_count',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ttl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.Security' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.Security',
            False, 
            [
            _MetaInfoClassMember('ttl', REFERENCE_CLASS, 'Ttl' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.Security.Ttl', 
                [], [], 
                '''                Enabling turns on TTL security
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'security',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('maximum-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Maximum path cost to remote LFA
                ''',
                'maximum_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tunnel', REFERENCE_ENUM_CLASS, 'OspfFrrRlfaTunnelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFrrRlfaTunnelEnum', 
                [], [], 
                '''                Enable/Disable remote LFA computation
                ''',
                'tunnel',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.RemoteLfa', 
                [], [], 
                '''                Remote LFA configuration
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('topology-independent-lfa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Topology Independet LFA configuration
                ''',
                'topology_independent_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'OspfFastRerouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.ProcessScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.ProcessScope',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF demand circuit
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable an OSPF area to advertise
                intra-area prefixes out of this area as external
                ''',
                'external_out',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-auto-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS LDP Auto Config
                ''',
                'ldp_auto_config',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync-igp-shortcuts', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync for igp-shortcuts
                ''',
                'ldp_sync_igp_shortcuts',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('link-down-fast-detect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable registration for early interface
                down notifications
                ''',
                'link_down_fast_detect',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('loopback-stub-network', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable advertising loopback as a stub
                network
                ''',
                'loopback_stub_network',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('network-type', REFERENCE_ENUM_CLASS, 'OspfNetworkEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfNetworkEnum', 
                [], [], 
                '''                Type of attached network
                ''',
                'network_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-suppression-secondary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable prefix suppression for secondary
                addresses
                ''',
                'prefix_suppression_secondary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Router priority for DR and BDR election
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('security', REFERENCE_CLASS, 'Security' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.Security', 
                [], [], 
                '''                Container class for security related
                configuration parameters
                ''',
                'security',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingEnum', 
                [], [], 
                '''                segment-routing configuration Applicable only in
                Default VRF
                ''',
                'segment_routing',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing-forwarding', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingForwardingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingForwardingEnum', 
                [], [], 
                '''                segment-routing forwarding configuration
                Applicableonly in Default VRF
                ''',
                'segment_routing_forwarding',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('srgb', REFERENCE_CLASS, 'Srgb' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope.Srgb', 
                [], [], 
                '''                Segment Routing Global Block configuration
                ''',
                'srgb',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-in', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable an OSPF area to advertise
                external prefixes into this area as summary
                ''',
                'summary_in',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'process-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.ConnectedOrStaticOrDagrOrSubscriberOrMobileOrRip' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.ConnectedOrStaticOrDagrOrSubscriberOrMobileOrRip',
            False, 
            [
            _MetaInfoClassMember('bgp-preserve-default-info', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve Metric and Metric Type of BGP
                Default Route
                ''',
                'bgp_preserve_default_info',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bgp-preserve-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve MED of BGP routes
                ''',
                'bgp_preserve_med',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('classful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disallow subnetting
                ''',
                'classful',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-redistributed-route-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                Default metric for routes being
                redistributed into OSPF
                ''',
                'default_redistributed_route_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'OspfEigrpRouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfEigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('isis-levels', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                Levels of ISIS routes
                ''',
                'isis_levels',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                Set OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-external', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF external route types
                ''',
                'ospf_external',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-internal', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                OSPF_Internal route type
                ''',
                'ospf_internal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-nssa-level', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF NSSA external route types
                ''',
                'ospf_nssa_level',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-redist-lsa-type', REFERENCE_ENUM_CLASS, 'OspfRedistLsaEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRedistLsaEnum', 
                [], [], 
                '''                LSA type for redistributed routes
                ''',
                'ospf_redist_lsa_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospfnssa-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only redistribute to NSSA areas
                ''',
                'ospfnssa_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Routing policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Set tag for routes redistributed into OSPF
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'connected-or-static-or-dagr-or-subscriber-or-mobile-or-rip',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.ApplicationOrIsisOrOspf' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.ApplicationOrIsisOrOspf',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF or ISIS process name or protocol name:
                bgp, eigrp, connected
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('bgp-preserve-default-info', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve Metric and Metric Type of BGP
                Default Route
                ''',
                'bgp_preserve_default_info',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bgp-preserve-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve MED of BGP routes
                ''',
                'bgp_preserve_med',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('classful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disallow subnetting
                ''',
                'classful',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-redistributed-route-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                Default metric for routes being
                redistributed into OSPF
                ''',
                'default_redistributed_route_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'OspfEigrpRouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfEigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('isis-levels', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                Levels of ISIS routes
                ''',
                'isis_levels',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                Set OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-external', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF external route types
                ''',
                'ospf_external',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-internal', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                OSPF_Internal route type
                ''',
                'ospf_internal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-nssa-level', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF NSSA external route types
                ''',
                'ospf_nssa_level',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-redist-lsa-type', REFERENCE_ENUM_CLASS, 'OspfRedistLsaEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRedistLsaEnum', 
                [], [], 
                '''                LSA type for redistributed routes
                ''',
                'ospf_redist_lsa_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospfnssa-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only redistribute to NSSA areas
                ''',
                'ospfnssa_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Routing policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Set tag for routes redistributed into OSPF
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'application-or-isis-or-ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.Bgp' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.Bgp',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                First half of BGP AS number in XX.YY format.
                Mandatory if Protocol is BGP and must not be
                specified otherwise. Must be a non-zero
                value if second half is zero.
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Second half of BGP AS number in XX.YY format
                . Mandatory if Protocol is BGP or EIGRP and
                must not be specified otherwise. Must be a
                non-zero value if first half is zero.
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF or ISIS process name or protocol name:
                bgp, eigrp, connected
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('bgp-preserve-default-info', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve Metric and Metric Type of BGP
                Default Route
                ''',
                'bgp_preserve_default_info',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bgp-preserve-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve MED of BGP routes
                ''',
                'bgp_preserve_med',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('classful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disallow subnetting
                ''',
                'classful',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-redistributed-route-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                Default metric for routes being
                redistributed into OSPF
                ''',
                'default_redistributed_route_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'OspfEigrpRouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfEigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('isis-levels', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                Levels of ISIS routes
                ''',
                'isis_levels',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                Set OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-external', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF external route types
                ''',
                'ospf_external',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-internal', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                OSPF_Internal route type
                ''',
                'ospf_internal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-nssa-level', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF NSSA external route types
                ''',
                'ospf_nssa_level',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-redist-lsa-type', REFERENCE_ENUM_CLASS, 'OspfRedistLsaEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRedistLsaEnum', 
                [], [], 
                '''                LSA type for redistributed routes
                ''',
                'ospf_redist_lsa_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospfnssa-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only redistribute to NSSA areas
                ''',
                'ospfnssa_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Routing policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Set tag for routes redistributed into OSPF
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.Eigrp' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.Eigrp',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                First half of BGP AS number in XX.YY format.
                Mandatory if Protocol is BGP and must not be
                specified otherwise. Must be a non-zero
                value if second half is zero.
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF or ISIS process name or protocol name:
                bgp, eigrp, connected
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('bgp-preserve-default-info', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve Metric and Metric Type of BGP
                Default Route
                ''',
                'bgp_preserve_default_info',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bgp-preserve-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve MED of BGP routes
                ''',
                'bgp_preserve_med',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('classful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disallow subnetting
                ''',
                'classful',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-redistributed-route-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                Default metric for routes being
                redistributed into OSPF
                ''',
                'default_redistributed_route_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'OspfEigrpRouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfEigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('isis-levels', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                Levels of ISIS routes
                ''',
                'isis_levels',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                Set OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-external', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF external route types
                ''',
                'ospf_external',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-internal', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                OSPF_Internal route type
                ''',
                'ospf_internal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-nssa-level', REFERENCE_ENUM_CLASS, 'OspfRouteLevelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRouteLevelEnum', 
                [], [], 
                '''                OSPF NSSA external route types
                ''',
                'ospf_nssa_level',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-redist-lsa-type', REFERENCE_ENUM_CLASS, 'OspfRedistLsaEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRedistLsaEnum', 
                [], [], 
                '''                LSA type for redistributed routes
                ''',
                'ospf_redist_lsa_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospfnssa-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only redistribute to NSSA areas
                ''',
                'ospfnssa_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Routing policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Set tag for routes redistributed into OSPF
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'eigrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'OspfRedistProtocolEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfRedistProtocolEnum', 
                [], [], 
                '''                Distribute list protocol type
                ''',
                'protocol_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('application-or-isis-or-ospf', REFERENCE_LIST, 'ApplicationOrIsisOrOspf' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.ApplicationOrIsisOrOspf', 
                [], [], 
                '''                application or isis or ospf
                ''',
                'application_or_isis_or_ospf',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bgp', REFERENCE_LIST, 'Bgp' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.Bgp', 
                [], [], 
                '''                bgp
                ''',
                'bgp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('connected-or-static-or-dagr-or-subscriber-or-mobile-or-rip', REFERENCE_CLASS, 'ConnectedOrStaticOrDagrOrSubscriberOrMobileOrRip' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.ConnectedOrStaticOrDagrOrSubscriberOrMobileOrRip', 
                [], [], 
                '''                connected or static or dagr or subscriber or
                mobile or rip
                ''',
                'connected_or_static_or_dagr_or_subscriber_or_mobile_or_rip',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('eigrp', REFERENCE_LIST, 'Eigrp' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.Eigrp', 
                [], [], 
                '''                eigrp
                ''',
                'eigrp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'redistribute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes',
            False, 
            [
            _MetaInfoClassMember('redistribute', REFERENCE_LIST, 'Redistribute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute', 
                [], [], 
                '''                Redistribute information from another routing
                protocol
                ''',
                'redistribute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'redistributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Redistribution' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Redistribution',
            False, 
            [
            _MetaInfoClassMember('redistributes', REFERENCE_CLASS, 'Redistributes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes', 
                [], [], 
                '''                Redistribute information from another routing
                protocol
                ''',
                'redistributes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'redistribution',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AdjacencyStagger' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AdjacencyStagger',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable OSPF adjacency stagger
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('initial-nbr', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Adjacency Stagger: Initial number of neighbors
                to bring up per area
                ''',
                'initial_nbr',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-nbr', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Adjacency Stagger: Subsequent simultaneous
                number of neighbors to bring up
                ''',
                'max_nbr',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'adjacency-stagger',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.MaxLsa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.MaxLsa',
            False, 
            [
            _MetaInfoClassMember('max-lsa-ignore-count', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967294)], [], 
                '''                Set count on how many times adjacencies can be
                suppressed
                ''',
                'max_lsa_ignore_count',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-lsa-ignore-time', ATTRIBUTE, 'int' , None, None, 
                [(1, 35791394)], [], 
                '''                Set time during which all adjacencies are
                suppressed
                ''',
                'max_lsa_ignore_time',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-lsa-limit', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967294)], [], 
                '''                Set maximum number of non self-generated LSAs
                ''',
                'max_lsa_limit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-lsa-reset-time', ATTRIBUTE, 'int' , None, None, 
                [(2, 71582788)], [], 
                '''                Set number of minutes after which ignore-count
                is reset to zero
                ''',
                'max_lsa_reset_time',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-lsa-threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Set max-lsa threshold for generating a warning
                message
                ''',
                'max_lsa_threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-lsa-warning-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Only give warning message when limit is
                exceeded
                ''',
                'max_lsa_warning_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'max-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AutoCost' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AutoCost',
            False, 
            [
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                The reference bandwidth in terms of Mbits per
                second
                ''',
                'bandwidth',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disabling auto costing
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'auto-cost',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Ucmp.Enable' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Ucmp.Enable',
            False, 
            [
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Prefix List
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('variance', ATTRIBUTE, 'int' , None, None, 
                [(101, 10000)], [], 
                '''                Value of variance
                ''',
                'variance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'enable',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Ucmp.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Ucmp.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Ucmp.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Ucmp.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Ucmp.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Ucmp' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Ucmp',
            False, 
            [
            _MetaInfoClassMember('delay-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 5000)], [], 
                '''                Delay in msecs between primary SPF and UCMP
                computation
                ''',
                'delay_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('enable', REFERENCE_CLASS, 'Enable' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Ucmp.Enable', 
                [], [], 
                '''                UCMP feature enable configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Ucmp.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ucmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'OspfFastReroutePriorityEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastReroutePriorityEnum', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix priority-limit
                command
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker',
            False, 
            [
            _MetaInfoClassMember('tiebreaker-type', REFERENCE_ENUM_CLASS, 'OspfFastRerouteTiebreakersEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastRerouteTiebreakersEnum', 
                [], [], 
                '''                Tiebreaker type
                ''',
                'tiebreaker_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('tiebreaker-index', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Index value for a tiebreaker
                ''',
                'tiebreaker_index',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'tiebreaker',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers',
            False, 
            [
            _MetaInfoClassMember('tiebreaker', REFERENCE_LIST, 'Tiebreaker' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker', 
                [], [], 
                '''                Fast-reroute tiebreakers configuration
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'tiebreakers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('load-sharing-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable load sharing between multiple backups
                ''',
                'load_sharing_disable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'OspfFastReroutePriorityEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastReroutePriorityEnum', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix priority-limit
                command
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tiebreakers', REFERENCE_CLASS, 'Tiebreakers' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers', 
                [], [], 
                '''                Fast-reroute tiebreakers configurations
                ''',
                'tiebreakers',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.FastReroute',
            False, 
            [
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link global configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix global configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.SummaryPrefixData' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.SummaryPrefixData',
            False, 
            [
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise when translating OSPF type-7
                LSA
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                32-bit tag value
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'summary-prefix-data',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.PrefixAndNetmask' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.PrefixAndNetmask',
            False, 
            [
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Summary netmask
                ''',
                'netmask',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP summary prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise when translating OSPF type-7
                LSA
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                32-bit tag value
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'prefix-and-netmask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.Prefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.Prefix',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP summary prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise when translating OSPF type-7
                LSA
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                32-bit tag value
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.Netmask' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.Netmask',
            False, 
            [
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Summary netmask
                ''',
                'netmask',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise when translating OSPF type-7
                LSA
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                32-bit tag value
                ''',
                'tag',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'netmask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.SummaryPrefixes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.SummaryPrefixes',
            False, 
            [
            _MetaInfoClassMember('netmask', REFERENCE_LIST, 'Netmask' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.Netmask', 
                [], [], 
                '''                keys: netmask
                ''',
                'netmask',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix', REFERENCE_LIST, 'Prefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.Prefix', 
                [], [], 
                '''                keys: prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-and-netmask', REFERENCE_LIST, 'PrefixAndNetmask' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.PrefixAndNetmask', 
                [], [], 
                '''                keys: prefix, netmask
                ''',
                'prefix_and_netmask',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-prefix-data', REFERENCE_CLASS, 'SummaryPrefixData' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.SummaryPrefixData', 
                [], [], 
                '''                Data container.
                ''',
                'summary_prefix_data',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'summary-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.OutgoingRouteUpdates.OutgoingRouteUpdate' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.OutgoingRouteUpdates.OutgoingRouteUpdate',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'OspfDistListProtocolEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfDistListProtocolEnum', 
                [], [], 
                '''                Distribute list protocol type
                ''',
                'protocol_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                First half of BGP AS number in XX.YY format. 
                Mandatory if Protocol is BGP and must not be
                specified otherwise. Must be a non-zero value
                if second half is zero.
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Second half of BGP AS number in XX.YY format.
                Mandatory if Protocol is BGP and must not be
                specified otherwise. Must be a non-zero value
                if first half is zero.
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF process name
                ''',
                'ospf_process_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'outgoing-route-update',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.OutgoingRouteUpdates' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.OutgoingRouteUpdates',
            False, 
            [
            _MetaInfoClassMember('outgoing-route-update', REFERENCE_LIST, 'OutgoingRouteUpdate' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.OutgoingRouteUpdates.OutgoingRouteUpdate', 
                [], [], 
                '''                Filter outgoing routing updates for a
                particular protocol
                ''',
                'outgoing_route_update',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'outgoing-route-updates',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Distance.OspfDistance' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Distance.OspfDistance',
            False, 
            [
            _MetaInfoClassMember('external-routes', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Distance for external type 5 and type 7 routes
                ''',
                'external_routes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('inter-area', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Distance for inter-area routes
                ''',
                'inter_area',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('intra-area', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Distance for intra-area routes
                ''',
                'intra_area',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ospf-distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Distance.IpDistances.IpDistance' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Distance.IpDistances.IpDistance',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP source address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('wildcard', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP wild card bits -- inverted mask
                ''',
                'wildcard',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ip-distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Distance.IpDistances' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Distance.IpDistances',
            False, 
            [
            _MetaInfoClassMember('ip-distance', REFERENCE_LIST, 'IpDistance' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Distance.IpDistances.IpDistance', 
                [], [], 
                '''                Administrative distance configuration for a
                particular IP address
                ''',
                'ip_distance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ip-distances',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Distance' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Distance',
            False, 
            [
            _MetaInfoClassMember('admin-distance', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Define an administrative distance
                ''',
                'admin_distance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ip-distances', REFERENCE_CLASS, 'IpDistances' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Distance.IpDistances', 
                [], [], 
                '''                IP specific administrative distance
                configuration
                ''',
                'ip_distances',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospf-distance', REFERENCE_CLASS, 'OspfDistance' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Distance.OspfDistance', 
                [], [], 
                '''                OSPF distance configuration
                ''',
                'ospf_distance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router ID of virtual link neighbor
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'virtual-link-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes',
            False, 
            [
            _MetaInfoClassMember('virtual-link-scope', REFERENCE_LIST, 'VirtualLinkScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope', 
                [], [], 
                '''                Virtual Link configuration
                ''',
                'virtual_link_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'virtual-link-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of the remote sham-link endpoint
                ''',
                'destination_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of the local sham-link endpoint
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of the local sham-link endpoint.
                Enter an IP Address
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'sham-link-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes',
            False, 
            [
            _MetaInfoClassMember('sham-link-scope', REFERENCE_LIST, 'ShamLinkScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope', 
                [], [], 
                '''                Sham Link configuration
                ''',
                'sham_link_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'sham-link-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 50)], [], 
                '''                Detection multiplier for BFD sessions created
                by OSPF
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'BfdEnableModeEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'BfdEnableModeEnum', 
                [], [], 
                '''                 use of Bidirectional Forwarding Detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(3, 30000)], [], 
                '''                Hello interval for BFD sessions created by OSPF
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Security.Ttl' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Security.Ttl',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable TTL security
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hop-count', ATTRIBUTE, 'int' , None, None, 
                [(1, 254)], [], 
                '''                Hop count
                ''',
                'hop_count',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ttl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Security' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Security',
            False, 
            [
            _MetaInfoClassMember('ttl', REFERENCE_CLASS, 'Ttl' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Security.Ttl', 
                [], [], 
                '''                Enabling turns on TTL security
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'security',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('maximum-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Maximum path cost to remote LFA
                ''',
                'maximum_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tunnel', REFERENCE_ENUM_CLASS, 'OspfFrrRlfaTunnelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFrrRlfaTunnelEnum', 
                [], [], 
                '''                Enable/Disable remote LFA computation
                ''',
                'tunnel',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.RemoteLfa', 
                [], [], 
                '''                Remote LFA configuration
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('topology-independent-lfa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Topology Independet LFA configuration
                ''',
                'topology_independent_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'OspfFastRerouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF demand circuit
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-auto-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS LDP Auto Config
                ''',
                'ldp_auto_config',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync-igp-shortcuts', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync for igp-shortcuts
                ''',
                'ldp_sync_igp_shortcuts',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('link-down-fast-detect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable registration for early interface
                down notifications
                ''',
                'link_down_fast_detect',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('loopback-stub-network', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable advertising loopback as a stub
                network
                ''',
                'loopback_stub_network',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('network-type', REFERENCE_ENUM_CLASS, 'OspfNetworkEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfNetworkEnum', 
                [], [], 
                '''                Type of attached network
                ''',
                'network_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-suppression-secondary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable prefix suppression for secondary
                addresses
                ''',
                'prefix_suppression_secondary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Router priority for DR and BDR election
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('security', REFERENCE_CLASS, 'Security' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Security', 
                [], [], 
                '''                Container class for security related
                configuration parameters
                ''',
                'security',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing-forwarding', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingForwardingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingForwardingEnum', 
                [], [], 
                '''                segment-routing forwarding configuration
                Applicableonly in Default VRF
                ''',
                'segment_routing_forwarding',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.PrefixSid' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.PrefixSid',
            False, 
            [
            _MetaInfoClassMember('explicit-null', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Force Penultimate Hop To Send Explicit-Null
                Label
                ''',
                'explicit_null',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('sid-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 1048575)], [], 
                '''                SID value
                ''',
                'sid_value',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'OspfSidEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSidEnum', 
                [], [], 
                '''                OSPF SID Type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'prefix-sid',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 50)], [], 
                '''                Detection multiplier for BFD sessions created
                by OSPF
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'BfdEnableModeEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'BfdEnableModeEnum', 
                [], [], 
                '''                 use of Bidirectional Forwarding Detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(3, 30000)], [], 
                '''                Hello interval for BFD sessions created by OSPF
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security.Ttl' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security.Ttl',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable TTL security
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hop-count', ATTRIBUTE, 'int' , None, None, 
                [(1, 254)], [], 
                '''                Hop count
                ''',
                'hop_count',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ttl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security',
            False, 
            [
            _MetaInfoClassMember('ttl', REFERENCE_CLASS, 'Ttl' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security.Ttl', 
                [], [], 
                '''                Enabling turns on TTL security
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'security',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('maximum-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Maximum path cost to remote LFA
                ''',
                'maximum_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tunnel', REFERENCE_ENUM_CLASS, 'OspfFrrRlfaTunnelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFrrRlfaTunnelEnum', 
                [], [], 
                '''                Enable/Disable remote LFA computation
                ''',
                'tunnel',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa', 
                [], [], 
                '''                Remote LFA configuration
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('topology-independent-lfa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Topology Independet LFA configuration
                ''',
                'topology_independent_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'OspfFastRerouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                OSPF cost for point-to-multipoint neighbor
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Database filter: Filter OSPF LSA during
                synchronization and flooding for
                point-to-multipoint
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                OSPF dead router poll-interval in seconds
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                OSPF priority of non-broadcast neighbor
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors.Neighbor', 
                [], [], 
                '''                Router configuration information for a
                particular neighbor
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF demand circuit
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-auto-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS LDP Auto Config
                ''',
                'ldp_auto_config',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync-igp-shortcuts', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync for igp-shortcuts
                ''',
                'ldp_sync_igp_shortcuts',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('link-down-fast-detect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable registration for early interface
                down notifications
                ''',
                'link_down_fast_detect',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('loopback-stub-network', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable advertising loopback as a stub
                network
                ''',
                'loopback_stub_network',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors', 
                [], [], 
                '''                Neighbor router configuration information
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('network-type', REFERENCE_ENUM_CLASS, 'OspfNetworkEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfNetworkEnum', 
                [], [], 
                '''                Type of attached network
                ''',
                'network_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-sid', REFERENCE_CLASS, 'PrefixSid' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.PrefixSid', 
                [], [], 
                '''                Prefix SID
                ''',
                'prefix_sid',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-suppression-secondary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable prefix suppression for secondary
                addresses
                ''',
                'prefix_suppression_secondary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Router priority for DR and BDR election
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('security', REFERENCE_CLASS, 'Security' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security', 
                [], [], 
                '''                Container class for security related
                configuration parameters
                ''',
                'security',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing-forwarding', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingForwardingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingForwardingEnum', 
                [], [], 
                '''                segment-routing forwarding configuration
                Applicableonly in Default VRF
                ''',
                'segment_routing_forwarding',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'name-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes',
            False, 
            [
            _MetaInfoClassMember('name-scope', REFERENCE_LIST, 'NameScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope', 
                [], [], 
                '''                Name scope configuration
                ''',
                'name_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'name-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                OSPF cost for point-to-multipoint neighbor
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Database filter: Filter OSPF LSA during
                synchronization and flooding for
                point-to-multipoint
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                OSPF dead router poll-interval in seconds
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                OSPF priority of non-broadcast neighbor
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor', 
                [], [], 
                '''                Router configuration information for a
                particular neighbor
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of Multi Area Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors', 
                [], [], 
                '''                Neighbor router configuration information
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'multi-area-interface-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes',
            False, 
            [
            _MetaInfoClassMember('multi-area-interface-scope', REFERENCE_LIST, 'MultiAreaInterfaceScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope', 
                [], [], 
                '''                Multi Area Interface configuration
                ''',
                'multi_area_interface_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'multi-area-interface-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaRanges.AreaRange' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaRanges.AreaRange',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address to match
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP netmask for address
                ''',
                'netmask',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise this range
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-range',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaRanges' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaRanges',
            False, 
            [
            _MetaInfoClassMember('area-range', REFERENCE_LIST, 'AreaRange' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaRanges.AreaRange', 
                [], [], 
                '''                Ordering index
                ''',
                'area_range',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Nssa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Nssa',
            False, 
            [
            _MetaInfoClassMember('default-info-originate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Originate Type 7 default into NSSA area
                ''',
                'default_info_originate',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('no-redistribution', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                No redistribution into this NSSA area
                ''',
                'no_redistribution',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('no-summary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not send summary LSA into NSSA
                ''',
                'no_summary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('nssa-def-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                OSPF default metric
                ''',
                'nssa_def_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'nssa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Area ID if in IP address format
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('area-ranges', REFERENCE_CLASS, 'AreaRanges' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaRanges', 
                [], [], 
                '''                Summarize routes matching address/mask (border
                routers only)
                ''',
                'area_ranges',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('area-scope', REFERENCE_CLASS, 'AreaScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope', 
                [], [], 
                '''                Area scope configuration
                ''',
                'area_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Set the summary default-cost of a NSSA/stub
                area
                ''',
                'default_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable an OSPF area to advertise
                intra-area prefixes out of this area as external
                ''',
                'external_out',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mpls-traffic-eng', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure an OSPF area to run MPLS Traffic
                Engineering
                ''',
                'mpls_traffic_eng',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multi-area-interface-scopes', REFERENCE_CLASS, 'MultiAreaInterfaceScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes', 
                [], [], 
                '''                Multi Area Interface scope configurations
                ''',
                'multi_area_interface_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('name-scopes', REFERENCE_CLASS, 'NameScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes', 
                [], [], 
                '''                Name scope configurations
                ''',
                'name_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('nssa', REFERENCE_CLASS, 'Nssa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Nssa', 
                [], [], 
                '''                Specify area as a NSSA area
                ''',
                'nssa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure a route policy for inbound type-3
                lsa filtering
                ''',
                'route_policy_in',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure a route policy for outbound type-3
                lsa filtering
                ''',
                'route_policy_out',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingEnum', 
                [], [], 
                '''                segment-routing configuration Applicable only in
                Default VRF
                ''',
                'segment_routing',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('sham-link-scopes', REFERENCE_CLASS, 'ShamLinkScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes', 
                [], [], 
                '''                Sham Link scope configurations
                ''',
                'sham_link_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify the area as a stub area (send summary
                LSA stub area)
                ''',
                'stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-in', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable an OSPF area to advertise
                external prefixes into this area as summary
                ''',
                'summary_in',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-link-scopes', REFERENCE_CLASS, 'VirtualLinkScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes', 
                [], [], 
                '''                Virtual Link scope configurations
                ''',
                'virtual_link_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router ID of virtual link neighbor
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'virtual-link-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes',
            False, 
            [
            _MetaInfoClassMember('virtual-link-scope', REFERENCE_LIST, 'VirtualLinkScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope', 
                [], [], 
                '''                Virtual Link configuration
                ''',
                'virtual_link_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'virtual-link-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of the remote sham-link endpoint
                ''',
                'destination_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of the local sham-link endpoint
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of the local sham-link endpoint.
                Enter an IP Address
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'sham-link-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes',
            False, 
            [
            _MetaInfoClassMember('sham-link-scope', REFERENCE_LIST, 'ShamLinkScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope', 
                [], [], 
                '''                Sham Link configuration
                ''',
                'sham_link_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'sham-link-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 50)], [], 
                '''                Detection multiplier for BFD sessions created
                by OSPF
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'BfdEnableModeEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'BfdEnableModeEnum', 
                [], [], 
                '''                 use of Bidirectional Forwarding Detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(3, 30000)], [], 
                '''                Hello interval for BFD sessions created by OSPF
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Security.Ttl' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Security.Ttl',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable TTL security
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hop-count', ATTRIBUTE, 'int' , None, None, 
                [(1, 254)], [], 
                '''                Hop count
                ''',
                'hop_count',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ttl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Security' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Security',
            False, 
            [
            _MetaInfoClassMember('ttl', REFERENCE_CLASS, 'Ttl' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Security.Ttl', 
                [], [], 
                '''                Enabling turns on TTL security
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'security',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('maximum-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Maximum path cost to remote LFA
                ''',
                'maximum_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tunnel', REFERENCE_ENUM_CLASS, 'OspfFrrRlfaTunnelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFrrRlfaTunnelEnum', 
                [], [], 
                '''                Enable/Disable remote LFA computation
                ''',
                'tunnel',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.RemoteLfa', 
                [], [], 
                '''                Remote LFA configuration
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('topology-independent-lfa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Topology Independet LFA configuration
                ''',
                'topology_independent_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'OspfFastRerouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF demand circuit
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-auto-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS LDP Auto Config
                ''',
                'ldp_auto_config',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync-igp-shortcuts', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync for igp-shortcuts
                ''',
                'ldp_sync_igp_shortcuts',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('link-down-fast-detect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable registration for early interface
                down notifications
                ''',
                'link_down_fast_detect',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('loopback-stub-network', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable advertising loopback as a stub
                network
                ''',
                'loopback_stub_network',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('network-type', REFERENCE_ENUM_CLASS, 'OspfNetworkEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfNetworkEnum', 
                [], [], 
                '''                Type of attached network
                ''',
                'network_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-suppression-secondary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable prefix suppression for secondary
                addresses
                ''',
                'prefix_suppression_secondary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Router priority for DR and BDR election
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('security', REFERENCE_CLASS, 'Security' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Security', 
                [], [], 
                '''                Container class for security related
                configuration parameters
                ''',
                'security',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing-forwarding', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingForwardingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingForwardingEnum', 
                [], [], 
                '''                segment-routing forwarding configuration
                Applicableonly in Default VRF
                ''',
                'segment_routing_forwarding',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.PrefixSid' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.PrefixSid',
            False, 
            [
            _MetaInfoClassMember('explicit-null', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Force Penultimate Hop To Send Explicit-Null
                Label
                ''',
                'explicit_null',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('sid-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 1048575)], [], 
                '''                SID value
                ''',
                'sid_value',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'OspfSidEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSidEnum', 
                [], [], 
                '''                OSPF SID Type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'prefix-sid',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 50)], [], 
                '''                Detection multiplier for BFD sessions created
                by OSPF
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'BfdEnableModeEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'BfdEnableModeEnum', 
                [], [], 
                '''                 use of Bidirectional Forwarding Detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(3, 30000)], [], 
                '''                Hello interval for BFD sessions created by OSPF
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security.Ttl' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security.Ttl',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable TTL security
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hop-count', ATTRIBUTE, 'int' , None, None, 
                [(1, 254)], [], 
                '''                Hop count
                ''',
                'hop_count',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ttl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security',
            False, 
            [
            _MetaInfoClassMember('ttl', REFERENCE_CLASS, 'Ttl' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security.Ttl', 
                [], [], 
                '''                Enabling turns on TTL security
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'security',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('maximum-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Maximum path cost to remote LFA
                ''',
                'maximum_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('tunnel', REFERENCE_ENUM_CLASS, 'OspfFrrRlfaTunnelEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFrrRlfaTunnelEnum', 
                [], [], 
                '''                Enable/Disable remote LFA computation
                ''',
                'tunnel',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup or
                UCMP
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix or UCMP exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa', 
                [], [], 
                '''                Remote LFA configuration
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('topology-independent-lfa', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Topology Independet LFA configuration
                ''',
                'topology_independent_lfa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'OspfFastRerouteEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfFastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                OSPF cost for point-to-multipoint neighbor
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Database filter: Filter OSPF LSA during
                synchronization and flooding for
                point-to-multipoint
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                OSPF dead router poll-interval in seconds
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                OSPF priority of non-broadcast neighbor
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors.Neighbor', 
                [], [], 
                '''                Router configuration information for a
                particular neighbor
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF demand circuit
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable OSPF flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-auto-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS LDP Auto Config
                ''',
                'ldp_auto_config',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ldp-sync-igp-shortcuts', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync for igp-shortcuts
                ''',
                'ldp_sync_igp_shortcuts',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('link-down-fast-detect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable registration for early interface
                down notifications
                ''',
                'link_down_fast_detect',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('loopback-stub-network', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable advertising loopback as a stub
                network
                ''',
                'loopback_stub_network',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors', 
                [], [], 
                '''                Neighbor router configuration information
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('network-type', REFERENCE_ENUM_CLASS, 'OspfNetworkEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfNetworkEnum', 
                [], [], 
                '''                Type of attached network
                ''',
                'network_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-sid', REFERENCE_CLASS, 'PrefixSid' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.PrefixSid', 
                [], [], 
                '''                Prefix SID
                ''',
                'prefix_sid',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('prefix-suppression-secondary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable prefix suppression for secondary
                addresses
                ''',
                'prefix_suppression_secondary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Router priority for DR and BDR election
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('security', REFERENCE_CLASS, 'Security' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security', 
                [], [], 
                '''                Container class for security related
                configuration parameters
                ''',
                'security',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing-forwarding', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingForwardingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingForwardingEnum', 
                [], [], 
                '''                segment-routing forwarding configuration
                Applicableonly in Default VRF
                ''',
                'segment_routing_forwarding',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'name-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes',
            False, 
            [
            _MetaInfoClassMember('name-scope', REFERENCE_LIST, 'NameScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope', 
                [], [], 
                '''                Name scope configuration
                ''',
                'name_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'name-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Control List name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type',
            False, 
            [
            _MetaInfoClassMember('authen-type', REFERENCE_ENUM_CLASS, 'OspfAuthenticationEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfAuthenticationEnum', 
                [], [], 
                '''                Authentication type code 
                ''',
                'authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-authen-type', REFERENCE_ENUM_CLASS, 'OspfKeychainAuthEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfKeychainAuthEnum', 
                [], [], 
                '''                Keychain authentication type
                ''',
                'keychain_authen_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Keychain name
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey',
            False, 
            [
            _MetaInfoClassMember('key-id', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                Key ID
                ''',
                'key_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies',
            False, 
            [
            _MetaInfoClassMember('message-digest-key', REFERENCE_LIST, 'MessageDigestKey' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey', 
                [], [], 
                '''                Message digest authentication password (key)
                configuration
                ''',
                'message_digest_key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'message-digest-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Authentication key configuration
                ''',
                'key',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('message-digest-keies', REFERENCE_CLASS, 'MessageDigestKeies' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies', 
                [], [], 
                '''                Message digest authentication password (key)
                configurations, first 16 chars used
                ''',
                'message_digest_keies',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type', 
                [], [], 
                '''                Authentication type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                OSPF cost for point-to-multipoint neighbor
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Database filter: Filter OSPF LSA during
                synchronization and flooding for
                point-to-multipoint
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                OSPF dead router poll-interval in seconds
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                OSPF priority of non-broadcast neighbor
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor', 
                [], [], 
                '''                Router configuration information for a
                particular neighbor
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal',
            False, 
            [
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval size in seconds after which a neighbor
                is declared dead
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multiplier', ATTRIBUTE, 'int' , None, None, 
                [(3, 20)], [], 
                '''                Number of Hellos in one second
                ''',
                'multiplier',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'dead-interval-minimal',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Fallback cost of link
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967)], [], 
                '''                Bandwidth threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'cost-fallback',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of Multi Area Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication', 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('cost-fallback', REFERENCE_CLASS, 'CostFallback' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback', 
                [], [], 
                '''                Interface fallback cost
                ''',
                'cost_fallback',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPF LSA during synchronization and
                flooding
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('dead-interval-minimal', REFERENCE_CLASS, 'DeadIntervalMinimal' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal', 
                [], [], 
                '''                Interval after which a neighbor is declared dead
                ''',
                'dead_interval_minimal',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList', 
                [], [], 
                '''                Filter networks intalled to RIB (disable as ACL
                name means filtering is disabled)
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Interval between HELLO packets in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors', 
                [], [], 
                '''                Neighbor router configuration information
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [(576, 10000)], [], 
                '''                Customize size of OSPF packets upto MTU
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, prevent sending HELLO packets over
                link
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Time in seconds between retransmitting lost link
                state advertisements
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay transmission of LSAs
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'multi-area-interface-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes',
            False, 
            [
            _MetaInfoClassMember('multi-area-interface-scope', REFERENCE_LIST, 'MultiAreaInterfaceScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope', 
                [], [], 
                '''                Multi Area Interface configuration
                ''',
                'multi_area_interface_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'multi-area-interface-scopes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaRanges.AreaRange' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaRanges.AreaRange',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address to match
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP netmask for address
                ''',
                'netmask',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise this range
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-range',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaRanges' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaRanges',
            False, 
            [
            _MetaInfoClassMember('area-range', REFERENCE_LIST, 'AreaRange' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaRanges.AreaRange', 
                [], [], 
                '''                Ordering index
                ''',
                'area_range',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Nssa' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Nssa',
            False, 
            [
            _MetaInfoClassMember('default-info-originate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Originate Type 7 default into NSSA area
                ''',
                'default_info_originate',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'OspfLinkStateMetricEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLinkStateMetricEnum', 
                [], [], 
                '''                OSPF External metric type
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('no-redistribution', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                No redistribution into this NSSA area
                ''',
                'no_redistribution',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('no-summary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not send summary LSA into NSSA
                ''',
                'no_summary',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('nssa-def-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                OSPF default metric
                ''',
                'nssa_def_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'nssa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId',
            False, 
            [
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Area ID if in integer format
                ''',
                'area_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('area-ranges', REFERENCE_CLASS, 'AreaRanges' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaRanges', 
                [], [], 
                '''                Summarize routes matching address/mask (border
                routers only)
                ''',
                'area_ranges',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('area-scope', REFERENCE_CLASS, 'AreaScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope', 
                [], [], 
                '''                Area scope configuration
                ''',
                'area_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-cost', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777215)], [], 
                '''                Set the summary default-cost of a NSSA/stub
                area
                ''',
                'default_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('external-out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable an OSPF area to advertise
                intra-area prefixes out of this area as external
                ''',
                'external_out',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mpls-traffic-eng', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure an OSPF area to run MPLS Traffic
                Engineering
                ''',
                'mpls_traffic_eng',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('multi-area-interface-scopes', REFERENCE_CLASS, 'MultiAreaInterfaceScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes', 
                [], [], 
                '''                Multi Area Interface scope configurations
                ''',
                'multi_area_interface_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('name-scopes', REFERENCE_CLASS, 'NameScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes', 
                [], [], 
                '''                Name scope configurations
                ''',
                'name_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('nssa', REFERENCE_CLASS, 'Nssa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Nssa', 
                [], [], 
                '''                Specify area as a NSSA area
                ''',
                'nssa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure a route policy for inbound type-3
                lsa filtering
                ''',
                'route_policy_in',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('route-policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure a route policy for outbound type-3
                lsa filtering
                ''',
                'route_policy_out',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_ENUM_CLASS, 'OspfSegmentRoutingEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfSegmentRoutingEnum', 
                [], [], 
                '''                segment-routing configuration Applicable only in
                Default VRF
                ''',
                'segment_routing',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('sham-link-scopes', REFERENCE_CLASS, 'ShamLinkScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes', 
                [], [], 
                '''                Sham Link scope configurations
                ''',
                'sham_link_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify the area as a stub area (send summary
                LSA stub area)
                ''',
                'stub',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-in', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable an OSPF area to advertise
                external prefixes into this area as summary
                ''',
                'summary_in',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-link-scopes', REFERENCE_CLASS, 'VirtualLinkScopes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes', 
                [], [], 
                '''                Virtual Link scope configurations
                ''',
                'virtual_link_scopes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-area-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.AreaAddresses' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.AreaAddresses',
            False, 
            [
            _MetaInfoClassMember('area-address', REFERENCE_LIST, 'AreaAddress' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress', 
                [], [], 
                '''                Configuration for a particular area
                ''',
                'area_address',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('area-area-id', REFERENCE_LIST, 'AreaAreaId' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId', 
                [], [], 
                '''                Configuration for a particular area
                ''',
                'area_area_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'area-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Timers.SpfTimer' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Timers.SpfTimer',
            False, 
            [
            _MetaInfoClassMember('backoff-increment', ATTRIBUTE, 'int' , None, None, 
                [(1, 600000)], [], 
                '''                Number of milliseconds delay between
                successive SPF runs
                ''',
                'backoff_increment',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('initial-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 600000)], [], 
                '''                Number of milliseconds before first SPF run
                ''',
                'initial_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 600000)], [], 
                '''                Max number of milliseconds between consecutive
                SPF calculations
                ''',
                'max_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'spf-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Timers.LsaGenerationTimer' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Timers.LsaGenerationTimer',
            False, 
            [
            _MetaInfoClassMember('backoff-increment', ATTRIBUTE, 'int' , None, None, 
                [(1, 600000)], [], 
                '''                Number of milliseconds delay between
                successive LSA builds
                ''',
                'backoff_increment',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('initial-delay', ATTRIBUTE, 'int' , None, None, 
                [(0, 600000)], [], 
                '''                Number of milliseconds before generating first
                LSA
                ''',
                'initial_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-delay', ATTRIBUTE, 'int' , None, None, 
                [(1, 600000)], [], 
                '''                Max number of milliseconds between consecutive
                LSA builds 
                ''',
                'max_delay',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'lsa-generation-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf.Timers' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf.Timers',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-timer', ATTRIBUTE, 'int' , None, None, 
                [(50, 600000)], [], 
                '''                Number of ms between end of SPF and start of
                IPFRR computation
                ''',
                'fast_reroute_timer',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lsa-generation-timer', REFERENCE_CLASS, 'LsaGenerationTimer' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Timers.LsaGenerationTimer', 
                [], [], 
                '''                OSPF LSA timers (in milliseconds)
                ''',
                'lsa_generation_timer',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lsa-group-pacing', ATTRIBUTE, 'int' , None, None, 
                [(10, 1800)], [], 
                '''                LSA group pacing timer (Seconds between group
                of LSAs being refreshed or maxaged)
                ''',
                'lsa_group_pacing',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lsa-min-arrival', ATTRIBUTE, 'int' , None, None, 
                [(0, 600000)], [], 
                '''                MinLSArrival timer (minimum interval in
                milliseconds between accepting the same LSA)
                ''',
                'lsa_min_arrival',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lsa-pacing-flood', ATTRIBUTE, 'int' , None, None, 
                [(5, 100)], [], 
                '''                Seconds between group of LSAs being refreshed
                or maxaged
                ''',
                'lsa_pacing_flood',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lsa-refresh', ATTRIBUTE, 'int' , None, None, 
                [(1800, 2700)], [], 
                '''                How often self-originated LSAs should be
                refreshed
                ''',
                'lsa_refresh',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('spf-timer', REFERENCE_CLASS, 'SpfTimer' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Timers.SpfTimer', 
                [], [], 
                '''                OSPF SPF timers (in milliseconds)
                ''',
                'spf_timer',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process.DefaultVrf',
            False, 
            [
            _MetaInfoClassMember('adjacency-changes', REFERENCE_ENUM_CLASS, 'OspfLogAdjEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfLogAdjEnum', 
                [], [], 
                '''                Log changes in adjacency state
                ''',
                'adjacency_changes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('adjacency-stagger', REFERENCE_CLASS, 'AdjacencyStagger' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AdjacencyStagger', 
                [], [], 
                '''                Staggering OSPF adjacency bring up
                ''',
                'adjacency_stagger',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('af', REFERENCE_CLASS, 'Af' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Af', 
                [], [], 
                '''                OSPF address family
                ''',
                'af',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('area-addresses', REFERENCE_CLASS, 'AreaAddresses' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AreaAddresses', 
                [], [], 
                '''                Area configuration
                ''',
                'area_addresses',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('auto-cost', REFERENCE_CLASS, 'AutoCost' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.AutoCost', 
                [], [], 
                '''                Controls automatic cost based on bandwidth
                ''',
                'auto_cost',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-information', REFERENCE_CLASS, 'DefaultInformation' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.DefaultInformation', 
                [], [], 
                '''                Control distribution of default information
                ''',
                'default_information',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [(1, 16777214)], [], 
                '''                Set default metric of redistributed routes
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distance', REFERENCE_CLASS, 'Distance' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Distance', 
                [], [], 
                '''                Administrative distance configuration
                ''',
                'distance',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.FastReroute', 
                [], [], 
                '''                Fast-reroute instance scoped parameters
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ignore-mospf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Ignore MOSPF (Type 6) LSAs
                ''',
                'ignore_mospf',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-lsa', REFERENCE_CLASS, 'MaxLsa' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.MaxLsa', 
                [], [], 
                '''                Set max-lsa configuration
                ''',
                'max_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('max-metric', REFERENCE_CLASS, 'MaxMetric' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.MaxMetric', 
                [], [], 
                '''                Set maximum metric configuration
                ''',
                'max_metric',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('maximum-interfaces', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Max number of interfaces allowed to be
                configured
                ''',
                'maximum_interfaces',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [(1, 64)], [], 
                '''                Forward packets over multiple paths (number of
                paths)
                ''',
                'maximum_paths',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('maximum-redistribute-prefix', REFERENCE_CLASS, 'MaximumRedistributePrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.MaximumRedistributePrefix', 
                [], [], 
                '''                Maximum number of prefixes redistributed into
                OSPF
                ''',
                'maximum_redistribute_prefix',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('microloop', REFERENCE_CLASS, 'Microloop' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Microloop', 
                [], [], 
                '''                Microloop configuration
                ''',
                'microloop',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('monitor-convergence', REFERENCE_CLASS, 'MonitorConvergence' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.MonitorConvergence', 
                [], [], 
                '''                Enable convergence monitoring
                ''',
                'monitor_convergence',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Mpls', 
                [], [], 
                '''                Configure MPLS routing protocol parameters
                ''',
                'mpls',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('no-opaque', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable opaque LSAs
                ''',
                'no_opaque',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('nsf', REFERENCE_CLASS, 'Nsf' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Nsf', 
                [], [], 
                '''                Non Stop Forwarding configuration
                ''',
                'nsf',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('outgoing-route-updates', REFERENCE_CLASS, 'OutgoingRouteUpdates' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.OutgoingRouteUpdates', 
                [], [], 
                '''                Filter outgoing routing updates
                ''',
                'outgoing_route_updates',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('process-scope', REFERENCE_CLASS, 'ProcessScope' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.ProcessScope', 
                [], [], 
                '''                Process scope configuration
                ''',
                'process_scope',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('queue', REFERENCE_CLASS, 'Queue' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Queue', 
                [], [], 
                '''                Adjust OSPF input queue sizes and processing
                quantums
                ''',
                'queue',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('redistribution', REFERENCE_CLASS, 'Redistribution' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Redistribution', 
                [], [], 
                '''                Redistribute configurations
                ''',
                'redistribution',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router ID for this OSPF process. Enter an IP
                Address.
                ''',
                'router_id',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_CLASS, 'SegmentRouting' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.SegmentRouting', 
                [], [], 
                '''                Segment Routing instance scoped parameters
                ''',
                'segment_routing',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('snmp-context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF SNMP context configuration
                ''',
                'snmp_context',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('spf-prefix-priority', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure a route-policy for prioritizing RIB
                route install.
                ''',
                'spf_prefix_priority',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('summary-prefixes', REFERENCE_CLASS, 'SummaryPrefixes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.SummaryPrefixes', 
                [], [], 
                '''                Configure IP prefix summary
                ''',
                'summary_prefixes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Timers', 
                [], [], 
                '''                Adjust routing timers
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('type7', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Prefer type7 externals over type5
                ''',
                'type7',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ucmp', REFERENCE_CLASS, 'Ucmp' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf.Ucmp', 
                [], [], 
                '''                Unequal Cost Multi-ptah configuration
                ''',
                'ucmp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'default-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes.Process' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes.Process',
            False, 
            [
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name for this OSPF process
                ''',
                'process_name',
                'Cisco-IOS-XR-ipv4-ospf-cfg', True),
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.DefaultVrf', 
                [], [], 
                '''                Default VRF related configuration
                ''',
                'default_vrf',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('distribute', REFERENCE_CLASS, 'Distribute' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Distribute', 
                [], [], 
                '''                Enable distribution of LSAs into BGP
                ''',
                'distribute',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('nsr', REFERENCE_ENUM_CLASS, 'NsrEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'NsrEnum', 
                [], [], 
                '''                Enable non-stop routing
                ''',
                'nsr',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('protocol-shutdown', REFERENCE_ENUM_CLASS, 'OspfShutdownEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'OspfShutdownEnum', 
                [], [], 
                '''                Type of protocol shutdown
                ''',
                'protocol_shutdown',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable routing on an IP network
                ''',
                'running',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('snmp', REFERENCE_CLASS, 'Snmp' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Snmp', 
                [], [], 
                '''                OSPF SNMP configuration
                ''',
                'snmp',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Start OSPF configuration
                ''',
                'start',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process.Vrfs', 
                [], [], 
                '''                VRF related configuration
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'process',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Processes' : {
        'meta_info' : _MetaInfoClass('Ospf.Processes',
            False, 
            [
            _MetaInfoClassMember('process', REFERENCE_LIST, 'Process' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes.Process', 
                [], [], 
                '''                Configuration for a particular OSPF process and
                associated default VRF
                ''',
                'process',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'processes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf.Global' : {
        'meta_info' : _MetaInfoClass('Ospf.Global',
            False, 
            [
            _MetaInfoClassMember('dns-name-lookup', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Display OSPF router ids as DNS names
                ''',
                'dns_name_lookup',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
    'Ospf' : {
        'meta_info' : _MetaInfoClass('Ospf',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Global', 
                [], [], 
                '''                OSPF global configuration data
                ''',
                'global_',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('processes', REFERENCE_CLASS, 'Processes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg', 'Ospf.Processes', 
                [], [], 
                '''                Process related configuration
                ''',
                'processes',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ospf_cfg'
        ),
    },
}
_meta_table['Ospf.Processes.Process.Snmp.TrapRateLimit']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Snmp']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds.SecondaryDomainId']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.DomainId.PrimaryDomainId']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.DomainId']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.DomainId']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Microloop.Avoidance']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Microloop']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnProcRestart']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaxMetric']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnStartup']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaxMetric']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnProcMigration']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaxMetric']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricAlways']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaxMetric']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaxMetric.MaxMetricOnSwitchover']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaxMetric']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Security.Ttl']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Security']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.RemoteLfa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Srgb']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Bfd']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.Security']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.ConnectedOrStaticOrDagrOrSubscriberOrMobileOrRip']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.ApplicationOrIsisOrOspf']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.Bgp']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute.Eigrp']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes.Redistribute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution.Redistributes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Ucmp.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Ucmp.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Ucmp.Enable']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Ucmp']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Ucmp.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Ucmp']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.SummaryPrefixData']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.PrefixAndNetmask']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.Prefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes.Netmask']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.OutgoingRouteUpdates.OutgoingRouteUpdate']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.OutgoingRouteUpdates']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Distance.IpDistances.IpDistance']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Distance.IpDistances']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Distance.OspfDistance']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Distance']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Distance.IpDistances']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Distance']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Security.Ttl']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Security']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.RemoteLfa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Bfd']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.Security']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security.Ttl']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.PrefixSid']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Bfd']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaRanges.AreaRange']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaRanges']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinkScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinkScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.NameScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaRanges']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Nssa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Security.Ttl']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Security']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.RemoteLfa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Bfd']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.Security']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security.Ttl']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.PrefixSid']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Bfd']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaRanges.AreaRange']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaRanges']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinkScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinkScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.NameScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaRanges']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Nssa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Timers.SpfTimer']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Timers']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Timers.LsaGenerationTimer']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Timers']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.DomainId']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Microloop']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaximumRedistributePrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.DefaultInformation']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Af']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Queue']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaxMetric']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Nsf']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.ProcessScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Redistribution']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AdjacencyStagger']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.MaxLsa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AutoCost']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Ucmp']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.FastReroute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.SummaryPrefixes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.OutgoingRouteUpdates']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Distance']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.AreaAddresses']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf.Timers']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ospf.Processes.Process.Vrfs']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.SegmentRouting.SrPrefer']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.SegmentRouting']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Mpls.MplsRouterId']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Mpls']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Microloop.Avoidance']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Microloop']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnProcRestart']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.MaxMetric']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnStartup']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.MaxMetric']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnProcMigration']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.MaxMetric']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricAlways']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.MaxMetric']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.MaxMetric.MaxMetricOnSwitchover']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.MaxMetric']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.Security.Ttl']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.Security']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.RemoteLfa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.Srgb']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.Bfd']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.Security']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.FastReroute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.ConnectedOrStaticOrDagrOrSubscriberOrMobileOrRip']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.ApplicationOrIsisOrOspf']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.Bgp']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute.Eigrp']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes.Redistribute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution.Redistributes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Ucmp.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Ucmp.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Ucmp.Enable']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Ucmp']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Ucmp.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Ucmp']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.SummaryPrefixData']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.SummaryPrefixes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.PrefixAndNetmask']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.SummaryPrefixes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.Prefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.SummaryPrefixes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.SummaryPrefixes.Netmask']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.SummaryPrefixes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.OutgoingRouteUpdates.OutgoingRouteUpdate']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.OutgoingRouteUpdates']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Distance.IpDistances.IpDistance']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Distance.IpDistances']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Distance.OspfDistance']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Distance']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Distance.IpDistances']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Distance']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes.VirtualLinkScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes.ShamLinkScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Security.Ttl']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Security']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.RemoteLfa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Bfd']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.Security']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security.Ttl']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.PrefixSid']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Bfd']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Security']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.FastReroute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.Neighbors']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes.NameScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaRanges.AreaRange']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaRanges']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinkScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinkScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.NameScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.MultiAreaInterfaceScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaRanges']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Nssa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes.VirtualLinkScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes.ShamLinkScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Security.Ttl']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Security']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.RemoteLfa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Bfd']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.Security']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security.Ttl']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.RemoteLfa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.PrefixSid']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Bfd']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Security']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.FastReroute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.Neighbors']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes.NameScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies.MessageDigestKey']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.Type']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication.MessageDigestKeies']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DistributeList']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Authentication']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.Neighbors']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.DeadIntervalMinimal']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope.CostFallback']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes.MultiAreaInterfaceScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaRanges.AreaRange']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaRanges']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinkScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinkScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.NameScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.MultiAreaInterfaceScopes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaRanges']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Nssa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Timers.SpfTimer']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Timers']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Timers.LsaGenerationTimer']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf.Timers']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.MonitorConvergence']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.SegmentRouting']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Mpls']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Microloop']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.MaximumRedistributePrefix']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.DefaultInformation']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Af']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Queue']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.MaxMetric']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Nsf']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.ProcessScope']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Redistribution']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AdjacencyStagger']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.MaxLsa']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AutoCost']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Ucmp']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.FastReroute']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.SummaryPrefixes']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.OutgoingRouteUpdates']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Distance']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.AreaAddresses']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf.Timers']['meta_info'].parent =_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospf.Processes.Process.Snmp']['meta_info'].parent =_meta_table['Ospf.Processes.Process']['meta_info']
_meta_table['Ospf.Processes.Process.Distribute']['meta_info'].parent =_meta_table['Ospf.Processes.Process']['meta_info']
_meta_table['Ospf.Processes.Process.Vrfs']['meta_info'].parent =_meta_table['Ospf.Processes.Process']['meta_info']
_meta_table['Ospf.Processes.Process.DefaultVrf']['meta_info'].parent =_meta_table['Ospf.Processes.Process']['meta_info']
_meta_table['Ospf.Processes.Process']['meta_info'].parent =_meta_table['Ospf.Processes']['meta_info']
_meta_table['Ospf.Processes']['meta_info'].parent =_meta_table['Ospf']['meta_info']
_meta_table['Ospf.Global']['meta_info'].parent =_meta_table['Ospf']['meta_info']
