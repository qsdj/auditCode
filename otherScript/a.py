#!/usr/bin/env python
# -*- coding:utf-8 -*-

# from fortifyAudit import fortipy
import fortipy
import json
with fortipy.FPR("D:\\workspace\\auditCode\\reports\\fpr\\xxxxxx_orderCenter.fpr") as fpr:
    # print dir(fpr)
    # ['__class__', '__delattr__', '__dict__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__',
    #  '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__'
    #     , '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'build', 'called_with_no_def', 'close',
    #  'descriptions', 'engine_data', 'files', 'get_code_for', 'get_types_of_vulns', 'get_vulns_of_type', 'snippets', 'te
    #  mppath', 'vulnerabilities']

    # print dir(fpr.build)
    # ('build_id', 'number_of_files', 'loc', 'java_class_path', 'source_base_path', 'scan_time', 'source_files')

    # newfiles= []
    # for f in fpr.build.source_files:
    #    newfiles.append(dict(f._asdict()))
    # exit()

    # newloc = []
    # for loc in fpr.build.loc:
    #     # print
    #     newloc.append({loc.type:loc.value})
    # a= newloc.__str__()
    # print list(a)
    # import json
    # print json.dumps(json.loads(newloc))
    # exit()

    # print dir(fpr.snippets[0])
    # ['__add__', '__class__', '__contains__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__',
    #  '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__getstate__', '__gt__', '__hash__',
    #  '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__',
    #  '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__',
    #  '_asdict', '_fields', '_make', '_replace', 'count', 'file', 'id', 'index', 'line_end', 'line_start', 'text']

    # for desc in fpr.descriptions:
    #     print dir(desc)
    #     # print desc.abstract
    #     # print desc.content_type,desc.class_id,desc.references
    #     print desc.references
    #     # 'abstract', 'class_id', 'content_type', 'count', 'explanation', 'index', 'recommendations', 'references']
    #     exit()
    # exit()

    # snippet = fpr.get_snippet_of_id("3FB0CDB1CC18DB6AFE7FD1A32F687C08#app/Controllers/deliveryController.php:149:149")
    # print snippet[0]
    # print fpr.snippets[0]._asdict()['file']

    # OrderedDict([('id', '3FB0CDB1CC18DB6AFE7FD1A32F687C08#app/Controllers/deliveryController.php:149:149'),
    #              ('file', 'app/Controllers/deliveryController.php'),
    # ('line_start', '146'), ('line_end', '152'), (
    #              'text',
    #              '        //if (22 != $data[\'customer_id\'] && 1011 != $data[\'customer_id\']) {\n        //    return $response->getBody()->write("FAIL");\n        //}\n        $verifyString = md5($data[\'customer_id\'] . $this->secret[$data[\'customer_id\']] . $data[\'timestamp\'] . $data[\'body\']);\n        if ($data[\'signature\'] != $verifyString) {\n            return $response->getBody()->write("FAIL, VERIFY");\n        }\n')])

    # exit()

    # print dir(fpr.vulnerabilities[0])
    # '_asdict', '_fields', '_make', '_replace', 'analysis_info', 'class_info', 'count', 'index', 'instance_info'
    for i in fpr.vulnerabilities:
        # print json.dumps(dict(i.analysis_info._asdict()),indent=4)
        # {'replacement_defs': ReplacementDefinitions(items=[KeyValue(key='PrimaryCall.name', value='mt_rand()'), KeyValue(key='PrimaryLocation.file', value='WxPayApi.php'), KeyValue(key='PrimaryLocation.line', value='490')], location=Location(path='lib/Payment/WxPayAPI/Lib/WxPayApi.php', line_start='490', line_end='490', col_start='0', col_end='0')), 'context': Context(function_name='getnoncestr', namespace='lib~^~payment~^~wxpayapi~^~lib', enclosing_class='wxpayapi', decl_location=Location(path='lib/Payment/WxPayAPI/Lib/WxPayApi.php', line_start='487', line_end='492', col_start='3', col_end='0')), 'trace': Trace(nodes=[Node(is_default=True, snippet_id='8284624FBCC4682B78BBBF60AD4057BB#lib/Payment/WxPayAPI/Lib/WxPayApi.php:490:490', source_location=Location(path='lib/Payment/WxPayAPI/Lib/WxPayApi.php', line_start='490', line_end='490', col_start='0', col_end='0'), action=TypeValue(type='InCall', value='mt_rand()'), reason='C01340E7-9E93-4C5C-B866-789891647627', knowledge=[])], nodes_ref=[])}
        # print dir(i.analysis_info.replacement_defs.items)
        
        # print type(i.analysis_info.trace)
        # print dir(i.analysis_info.trace)
        # print dict(i.analysis_info.trace._asdict())
        # {'nodes': [Node(is_default=True, snippet_id='AA745D3DB840CD3BBBCAAFC1F9D796E5#lib/Payment/AliPayAPI/Lib/Sign.php:32:32', source_location=Location(path='lib/Payment/AliPayAPI/Lib/Sign.php', line_start='32', line_end='32', col_start='0', col_end='0'), action=TypeValue(type='InCall', value='md5()'), reason='3E15CC2F-6FD3-405F-BEF8-2F0E7B30945A', knowledge=[])], 'nodes_ref': []}
        # nodes = i.analysis_info.trace.nodes[0]._asdict()
        # # print i.analysis_info.trace.nodes.__len__()
        # # continue
        # print nodes
        # for node in i.analysis_info.trace.nodes:
        #     if node._asdict().has_key("source_location"):
        #         nodes['source_location']=node.source_location._asdict()
        #     if node._asdict().has_key("action"):
        #         if nodes['action'] is not None:
        #             nodes['action']=node.action._asdict()
        # print nodes
        newNodesRef={'id':""}
        if i.analysis_info.trace.nodes_ref is not None:
            newNodesRef['id']=[node_ref.id for node_ref in i.analysis_info.trace.nodes_ref]
            # for node_ref in nodes_ref:
            #     print node_ref.id
            # nodes_ref['id']=[node_ref.id for node_ref in nodes_ref]
            # newNodesRef['id']=[node_ref.id for node_ref in i.analysis_info.trace.nodes_ref]
        # print newNodesRef['id'].__len__()
        print newNodesRef['id'] is None
    exit()

    # ReplacementDefinitions = {}
    # if i.analysis_info.replacement_defs is not None:
    #     for item in i.analysis_info.replacement_defs:
    #         if item is None:
    #             continue
    #         if isinstance(item, list):
    #             for i in item:
    #                 ReplacementDefinitions[i.key] = i.value
    #         else:
    #             ReplacementDefinitions.update(dict(item._asdict()))
    # print json.dumps(ReplacementDefinitions, indent=4)

    # OrderedDict([('class_id', '4C36222E-0455-451f-9D51-7B15E2B713FA'), ('kingdom', 'Encapsulation'),
    #              ('type', 'System Information Leak'), ('subtype', 'External'), ('analyzer_name', 'semantic'),
    #              ('default_severity', '3.0')])

        # print dict(i.analysis_info._asdict())
        # {'replacement_defs': None,
        #  'context': Context(function_name='md5sign', namespace='lib~^~payment~^~alipayapi~^~lib',
        #                     enclosing_class='sign',
        #                     decl_location=Location(path='lib/Payment/AliPayAPI/Lib/Sign.php', line_start='31',
        #                                            line_end='32', col_start='9', col_end='0')), 'trace': Trace(nodes=[
        #     Node(is_default=True,
        #          snippet_id='AA745D3DB840CD3BBBCAAFC1F9D796E5#lib/Payment/AliPayAPI/Lib/Sign.php:32:32',
        #          source_location=Location(path='lib/Payment/AliPayAPI/Lib/Sign.php', line_start='32', line_end='32',
        #                                   col_start='0', col_end='0'), action=TypeValue(type='InCall', value='md5()'),
        # reason='3E15CC2F-6FD3-405F-BEF8-2F0E7B30945A', knowledge=[])],
        # nodes_ref=[])}
        # print i.analysis_info.context._asdict()
        # print i.analysis_info.trace._asdict()
        # print i.analysis_info.trace.nodes[0].snippet_id
        # print i.analysis_info.trace.nodes_ref
        # print i.s
    print
    print dict(fpr.build._asdict()).keys()
    print type(fpr.build.loc[0])
    exit()
    # for d in fpr.snippets:
    #     print "=" * 60
    #     print d.id, d.file, d.line_start, d.line_end
    #     print d.text
    #     print "=" * 60
    for i in fpr.get_vulns_of_type("Password Management"):
        print i.class_info
        # print dir(i)
        # ['__add__', '__class__', '__contains__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__',
        #  '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__getstate__', '__gt__', '__hash__',
        #  '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__',
        #  '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__slots__', '__str__',
        #  '__subclasshook__', '_asdict', '_fields', '_make', '_replace', 'analysis_info', 'class_info', 'count', 'index',
        #  'instance_info']
        # print i.analysis_info.trace.nodes[0].snippet_id
