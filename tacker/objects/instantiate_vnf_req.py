# Copyright (C) 2020 NTT DATA
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_log import log as logging

from tacker import objects
from tacker.objects import base
from tacker.objects import fields

LOG = logging.getLogger(__name__)


@base.TackerObjectRegistry.register
class InstantiateVnfRequest(base.TackerObject):
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        'flavour_id': fields.StringField(nullable=False),
        'instantiation_level_id': fields.StringField(nullable=True,
                                                     default=None),
        'ext_managed_virtual_links': fields.ListOfObjectsField(
            'ExtManagedVirtualLinkData', nullable=True, default=[]),
        'vim_connection_info': fields.ListOfObjectsField(
            'VimConnectionInfo', nullable=True, default=[]),
        'ext_virtual_links': fields.ListOfObjectsField(
            'ExtVirtualLinkData', nullable=True, default=[]),
        'additional_params': fields.DictOfStringsField(nullable=True,
            default={}),
    }

    @classmethod
    def obj_from_primitive(cls, primitive, context):
        if 'tacker_object.name' in primitive:
            obj_instantiate_vnf_req = super(
                InstantiateVnfRequest, cls).obj_from_primitive(
                primitive, context)
        else:
            if 'ext_managed_virtual_links' in primitive.keys():
                obj_data = [ExtManagedVirtualLinkData._from_dict(
                    ext_manage) for ext_manage in primitive.get(
                    'ext_managed_virtual_links', [])]
                primitive.update({'ext_managed_virtual_links': obj_data})

            if 'vim_connection_info' in primitive.keys():
                obj_data = [objects.VimConnectionInfo._from_dict(
                    vim_conn) for vim_conn in primitive.get(
                    'vim_connection_info', [])]
                primitive.update({'vim_connection_info': obj_data})

            if 'ext_virtual_links' in primitive.keys():
                obj_data = [ExtVirtualLinkData.obj_from_primitive(
                    ext_vir_link, context) for ext_vir_link in primitive.get(
                    'ext_virtual_links', [])]
                primitive.update({'ext_virtual_links': obj_data})
            obj_instantiate_vnf_req = InstantiateVnfRequest._from_dict(
                primitive)

        return obj_instantiate_vnf_req

    @classmethod
    def _from_dict(cls, data_dict):
        flavour_id = data_dict.get('flavour_id')
        instantiation_level_id = data_dict.get('instantiation_level_id')
        ext_managed_virtual_links = data_dict.get('ext_managed_virtual_links',
                                                  [])
        vim_connection_info = data_dict.get('vim_connection_info', [])
        ext_virtual_links = data_dict.get('ext_virtual_links', [])
        additional_params = data_dict.get('additional_params', {})

        return cls(flavour_id=flavour_id,
        instantiation_level_id=instantiation_level_id,
        ext_managed_virtual_links=ext_managed_virtual_links,
        vim_connection_info=vim_connection_info,
        ext_virtual_links=ext_virtual_links,
        additional_params=additional_params)


@base.TackerObjectRegistry.register
class ExtManagedVirtualLinkData(base.TackerObject):
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        'id': fields.StringField(nullable=False),
        'vnf_virtual_link_desc_id': fields.StringField(nullable=False),
        'resource_id': fields.StringField(nullable=False),
    }

    @classmethod
    def _from_dict(cls, data_dict):
        id = data_dict.get('id')
        vnf_virtual_link_desc_id = data_dict.get(
            'vnf_virtual_link_desc_id')
        resource_id = data_dict.get('resource_id')
        obj = cls(id=id, vnf_virtual_link_desc_id=vnf_virtual_link_desc_id,
                  resource_id=resource_id)
        return obj


@base.TackerObjectRegistry.register
class ExtVirtualLinkData(base.TackerObject):
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        'id': fields.StringField(nullable=False),
        'resource_id': fields.StringField(nullable=False),
        'ext_cps': fields.ListOfObjectsField(
            'VnfExtCpData', nullable=True, default=[]),
        'ext_link_ports': fields.ListOfObjectsField(
            'ExtLinkPortData', nullable=True, default=[]),
    }

    @classmethod
    def obj_from_primitive(cls, primitive, context):
        if 'tacker_object.name' in primitive:
            obj_ext_virt_link = super(
                ExtVirtualLinkData, cls).obj_from_primitive(
                primitive, context)
        else:
            if 'ext_cps' in primitive.keys():
                obj_data = [VnfExtCpData.obj_from_primitive(
                    ext_cp, context) for ext_cp in primitive.get(
                    'ext_cps', [])]
                primitive.update({'ext_cps': obj_data})

            if 'ext_link_ports' in primitive.keys():
                obj_data = [ExtLinkPortData.obj_from_primitive(
                    ext_link_port_data, context)
                    for ext_link_port_data in primitive.get(
                        'ext_link_ports', [])]
                primitive.update({'ext_link_ports': obj_data})

            obj_ext_virt_link = ExtVirtualLinkData._from_dict(primitive)

        return obj_ext_virt_link

    @classmethod
    def _from_dict(cls, data_dict):
        id = data_dict.get('id')
        resource_id = data_dict.get('resource_id')
        ext_cps = data_dict.get('ext_cps', [])
        ext_link_ports = data_dict.get('ext_link_ports', [])

        obj = cls(id=id, resource_id=resource_id, ext_cps=ext_cps,
                  ext_link_ports=ext_link_ports)
        return obj


@base.TackerObjectRegistry.register
class VnfExtCpData(base.TackerObject):
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        'cpd_id': fields.StringField(nullable=False),
        'cp_config': fields.ListOfObjectsField(
            'VnfExtCpConfig', nullable=True, default=[]),
    }

    @classmethod
    def obj_from_primitive(cls, primitive, context):
        if 'tacker_object.name' in primitive:
            obj_vnf_ext_cp_data = super(VnfExtCpData, cls).obj_from_primitive(
                primitive, context)
        else:
            if 'cp_config' in primitive.keys():
                obj_data = [VnfExtCpConfig.obj_from_primitive(
                    vnf_ext_cp_conf, context)
                    for vnf_ext_cp_conf in primitive.get('cp_config', [])]
                primitive.update({'cp_config': obj_data})

            obj_vnf_ext_cp_data = VnfExtCpData._from_dict(primitive)

        return obj_vnf_ext_cp_data

    @classmethod
    def _from_dict(cls, data_dict):
        cpd_id = data_dict.get('cpd_id')
        cp_config = data_dict.get('cp_config', [])

        obj = cls(cpd_id=cpd_id, cp_config=cp_config)
        return obj


@base.TackerObjectRegistry.register
class VnfExtCpConfig(base.TackerObject):
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        'cp_instance_id': fields.StringField(nullable=True, default=None),
        'link_port_id': fields.StringField(nullable=True, default=None),
        'cp_protocol_data': fields.ListOfObjectsField(
            'CpProtocolData', nullable=True, default=[]),
    }

    @classmethod
    def obj_from_primitive(cls, primitive, context):
        if 'tacker_object.name' in primitive:
            obj_ext_cp_config = super(VnfExtCpConfig, cls).obj_from_primitive(
                primitive, context)
        else:
            if 'cp_protocol_data' in primitive.keys():
                obj_data = [CpProtocolData.obj_from_primitive(
                    cp_protocol, context) for cp_protocol in primitive.get(
                    'cp_protocol_data', [])]
                primitive.update({'cp_protocol_data': obj_data})

            obj_ext_cp_config = VnfExtCpConfig._from_dict(primitive)

        return obj_ext_cp_config

    @classmethod
    def _from_dict(cls, data_dict):
        cp_instance_id = data_dict.get('cp_instance_id')
        link_port_id = data_dict.get('link_port_id')
        cp_protocol_data = data_dict.get('cp_protocol_data', [])

        obj = cls(cp_instance_id=cp_instance_id,
                  link_port_id=link_port_id, cp_protocol_data=cp_protocol_data)
        return obj


@base.TackerObjectRegistry.register
class CpProtocolData(base.TackerObject):
    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        'layer_protocol': fields.StringField(nullable=False),
        'ip_over_ethernet': fields.ObjectField(
            'IpOverEthernetAddressData', nullable=True, default=None),
    }

    @classmethod
    def obj_from_primitive(cls, primitive, context):
        if 'tacker_object.name' in primitive:
            obj_cp_protocal = super(CpProtocolData, cls).obj_from_primitive(
                primitive, context)
        else:
            if 'ip_over_ethernet' in primitive.keys():
                obj_data = IpOverEthernetAddressData.obj_from_primitive(
                    primitive.get('ip_over_ethernet', {}), context)
                primitive.update({'ip_over_ethernet': obj_data})
            obj_cp_protocal = CpProtocolData._from_dict(primitive)

        return obj_cp_protocal

    @classmethod
    def _from_dict(cls, data_dict):
        layer_protocol = data_dict.get('layer_protocol')
        ip_over_ethernet = data_dict.get('ip_over_ethernet')

        obj = cls(layer_protocol=layer_protocol,
                  ip_over_ethernet=ip_over_ethernet)
        return obj


@base.TackerObjectRegistry.register
class IpOverEthernetAddressData(base.TackerObject):

    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        'mac_address': fields.StringField(nullable=True, default=None),
        'ip_addresses': fields.ListOfObjectsField('IpAddress', nullable=True,
            default=[]),
    }

    @classmethod
    def obj_from_primitive(cls, primitive, context):
        if 'tacker_object.name' in primitive:
            ip_over_ethernet = super(
                IpOverEthernetAddressData, cls).obj_from_primitive(
                primitive, context)
        else:
            if 'ip_addresses' in primitive.keys():
                obj_data = [IpAddress._from_dict(
                    ip_address) for ip_address in primitive.get(
                        'ip_addresses', [])]
                primitive.update({'ip_addresses': obj_data})

            ip_over_ethernet = IpOverEthernetAddressData._from_dict(primitive)

        return ip_over_ethernet

    @classmethod
    def _from_dict(cls, data_dict):
        mac_address = data_dict.get('mac_address')
        ip_addresses = data_dict.get('ip_addresses', [])
        obj = cls(mac_address=mac_address, ip_addresses=ip_addresses)
        return obj


@base.TackerObjectRegistry.register
class IpAddress(base.TackerObject):

    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        'type': fields.IpAddressTypeField(nullable=False),
        'subnet_id': fields.StringField(nullable=True, default=None),
        'fixed_addresses': fields.ListOfStringsField(nullable=True,
            default=[])
    }

    @classmethod
    def _from_dict(cls, data_dict):
        type = data_dict.get('type')
        subnet_id = data_dict.get('subnet_id')
        fixed_addresses = data_dict.get('fixed_addresses', [])

        obj = cls(type=type, subnet_id=subnet_id,
                fixed_addresses=fixed_addresses)

        return obj


@base.TackerObjectRegistry.register
class ExtLinkPortData(base.TackerObject):

    # Version 1.0: Initial version
    VERSION = '1.0'

    fields = {
        'id': fields.UUIDField(nullable=False),
        'resource_handle': fields.ObjectField(
            'ResourceHandle', nullable=False),
    }

    @classmethod
    def obj_from_primitive(cls, primitive, context):
        if 'tacker_object.name' in primitive:
            obj_link_port_data = super(
                ExtLinkPortData, cls).obj_from_primitive(primitive, context)
        else:
            if 'resource_handle' in primitive.keys():
                obj_data = objects.ResourceHandle._from_dict(primitive.get(
                    'resource_handle', []))
                primitive.update({'resource_handle': obj_data})

            obj_link_port_data = ExtLinkPortData._from_dict(primitive)

        return obj_link_port_data

    @classmethod
    def _from_dict(cls, data_dict):
        id = data_dict.get('id')
        resource_handle = data_dict.get('resource_handle')

        obj = cls(id=id, resource_handle=resource_handle)
        return obj
