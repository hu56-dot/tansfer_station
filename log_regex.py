# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/11/10 01:40
# @Author  : echojarn@gamil.com
# @File    : log_regex.py
# Version: 1.0
# @Project : tansfer_station
# License: MIT
# description:
from typing import List, Literal


class RubyLogRegex:
    def __init__(self, log_content):
        self.full_log_content = log_content
        self.before_split_content = None
        self.after_split_content = None
        self.before_split_errsmg = None
        self.after_split_errmsg = None
        # 这个参数的列表里面的元素顺序依次为[before_errmsg,before_content,after_errmsg,after_content,full_content]
        # 每一个元素的类型是元组，分别代表被匹配的文本信息和匹配到的正则
        self.inference_out: List[tuple[str, None]] = None

    async def log_split(self, split_line_regex):
        """
        split log content by split_line

        Args:
            split_line (_type_): one line of split the log_content into two part
            
        Returns:
            list: a list of two part of log_content or [] if not found
            :param split_line_regex:
        """
        pass

    async def get_errmsg(self, text):
        """
        get error message from log content
        
        Args:
            text (str): log content
            
        Returns:
            str: error message or '' if not found
        """
        pass

    async def content_regex(self, regex: List, content: str, content_type: Literal['errmsg_content', 'normal_content']):
        """
        use regex to match content in log content
        
        Args:
            regex (List): a list of regex
            content (str): log content
            content_type (Literal): 'errmsg_content' or 'normal_content'
            
        Returns:
            tuple[str, None]: matched content and regex_content  or None if not found

        doc:
            if content_type == 'errmsg_content':
                '''
                如果是errmsg段，则将errmsg段作为content，
                '''
                pass
            else:
                '''
                如果是normal段，则将匹配到内容的前后五行作为content
                '''
                pass
        """

        pass

    async def regex_algorithm(self, content, regex_list):
        """
        此组件可以专门用于正则匹配算法的优化，比如使用前缀树，组合正则命名组、状态机等方式提高匹配效率
        :param content:
        :param regex_list:
        :return:
        """
        pass

    async def filter(self, content):
        """
        主要用于文本的杂质过滤，如不必要的换行符等等
        :param content:
        :return:
        """
        pass

    async def run(self):
        """
        日志正则匹配处理的主要逻辑入口

        :return:
        """
        pass


class RubyLogRegexTs(RubyLogRegex):
    def __init__(self, log_content):
        super().__init__(log_content)

    async def log_split(self, split_line_regex):
        """
        这里的分割正则主要依赖于 cleanup::begin 关键字
        :param split_line_regex:
        :return:
        """
        self.before_split_content = self.full_log_content.split(split_line_regex, 1)[0]
        self.after_split_content = self.full_log_content.split(split_line_regex, 1)[1]

    async def get_errmsg(self, text):
        """
        get error message from log content

        Args:
            text (str): log content

        Returns:
            str: error message or '' if not found
        """
        pass

    async def content_regex(self, regex: List, content: str, content_type: Literal['errmsg_content', 'normal_content']):
        """
        use regex to match content in log content

        Args:
            regex (List): a list of regex
            content (str): log content
            content_type (Literal): 'errmsg_content' or 'normal_content'

        Returns:
            tuple[str, None]: matched content and regex_content  or None if not found

        doc:
            if content_type == 'errmsg_content':
                '''
                如果是errmsg段，则将errmsg段作为content，
                '''
                pass
            else:
                '''
                如果是normal段，则将匹配到内容的前后五行作为content
                '''
                pass
        """

        pass

    async def regex_algorithm(self, content, regex_list):
        """
        此组件可以专门用于正则匹配算法的优化，比如使用前缀树，组合正则命名组、状态机等方式提高匹配效率
        :param content:
        :param regex_list:
        :return:
        """
        pass

    async def filter(self, content):
        """
        主要用于文本的杂质过滤，如不必要的换行符等等
        :param content:
        :return:
        """
        pass

    async def run(self):
        """
        日志正则匹配处理的主要逻辑入口

        :return:
        """
        pass


class RubyLogRegexTc(RubyLogRegex):
    def __init__(self, log_content):
        super().__init__(log_content)

    async def log_split(self, split_line_regex):
        """
        这里的分割正则主要依赖于 >>>>>>>>>>>>>>>>error message>>>>>>>>>>>>>>>>>> 段
        :param split_line_regex:
        :return:
        """
        self.before_split_content = self.full_log_content.split(split_line_regex, 1)[0]
        self.after_split_content = self.full_log_content.split(split_line_regex, 1)[1]

    async def get_errmsg(self, text):
        """
        get error message from log content

        Args:
            text (str): log content

        Returns:
            str: error message or '' if not found
        """
        pass

    async def content_regex(self, regex: List, content: str, content_type: Literal['errmsg_content', 'normal_content']):
        """
        use regex to match content in log content

        Args:
            regex (List): a list of regex
            content (str): log content
            content_type (Literal): 'errmsg_content' or 'normal_content'

        Returns:
            tuple[str, None]: matched content and regex_content  or None if not found

        doc:
            if content_type == 'errmsg_content':
                '''
                如果是errmsg段，则将errmsg段作为content，
                '''
                pass
            else:
                '''
                如果是normal段，则将匹配到内容的前后五行作为content
                '''
                pass
        """

        pass

    async def regex_algorithm(self, content, regex_list):
        """
        此组件可以专门用于正则匹配算法的优化，比如使用前缀树，组合正则命名组、状态机等方式提高匹配效率
        :param content:
        :param regex_list:
        :return:
        """
        pass

    async def filter(self, content):
        """
        主要用于文本的杂质过滤，如不必要的换行符等等
        :param content:
        :return:
        """
        pass

    async def run(self):
        """
        日志正则匹配处理的主要逻辑入口

        :return:
        """
        pass


"""
现在假设我们通过测试日志和测试套日志分别获取了最终的所有情况
对于当前的某一条日志，其最终形态应该如何返回:
首先定义专家结论类型：
    1、真实的专家结论的：就写对应的真实专家规则对象
    2、没有匹配到专家结论的：填写专家规则对象结构的默认空值
其次定义errmsg（既指error message段，又指正文被匹配到的错误信息前后5行的那个文本）：
    1、就正常的文本内容
    2、“未找到errmsg，且未匹配到对应的专家规则”

下面的列表的元素的结构为  元组(文本内容，正则条例)
ts_log_regex_out = [before_errmsg_ts,before_content_ts,after_errmsg_ts,after_content_ts,full_content_ts]
tc_log = [before_errmsg_tc,before_content_tc,after_errmsg_tc,after_content_tc,full_content_tc]

考虑最终的排序问题：
    1、假如所有的序列元素中至少一个有匹配结果的，按照下面的顺序，将第一个有匹配结果的元素作为最终值返回,其形态应该是(errmsg,regex_object)
    [
    before_errmsg_ts,before_content_ts,     
    before_errmsg_tc,before_content_tc,after_errmsg_tc,after_content_tc,full_content_tc,
    after_errmsg_ts,after_content_ts,full_content_ts
    ]
    2、假如全都没有匹配结果的，按照下面的顺序，返回首个对应的元素,其形态应该是(errmsg,None)
    [before_errmsg_tc,after_errmsg_tc,before_errmsg_ts,after_errmsg_ts]
    3、假如这些元素（也就是errmsg段都没有的）
        就返回("“未找到errmsg，且未匹配到对应的专家规则”",None)
        
        

"""

"""
# 实际上获取errmsg和进行专家推理的接口形态，应该公用一套逻辑才对
# 各个接口模块的要求，
1、全量支持批量，
2、放弃无用参数，用户接口只给与简单的接口查询参数，
3、其他的数据字段的获取尽量依赖于后台去关键数据库的查询，
4、要写出尽可能多的隔离接口

# 首先定义一个完整的推理流程 full_inference： 获取errmsg、走专家推理、走机器学习推理《要求这些模块在某些时刻需要协同配合，有些时刻又能各自独立运行》（这里利用的errmsg是前一步专家推理的落库的errmsg数据）【以及各个阶段的落库的动作和异常解析过程的落库（日志文本内容解析失败、）】
# 对于获取errmsg：
    # 查数据库，
        # 有记录，直接返回
    # 无记录，直接走full_inference
        # 查errmsg库，并返回
    
# 对于专家经验推理：
    # 首先是查库，
        # 有记录直接返回
    # 无记录直接走full_inference
        # 查库并返回
        
# 对于专家经验推理重跑，
    # 直接重走full_inference
    
# 对于向量检索分析：
    # 先查库，
        # 如果有记录，则直接返回，
        # 如果没有，则直接重走full_inference(前提是不存在前两层推理过后，第三层却没记录的情况，因此无论什么情况发生，都一定要保证三个结论表都有数据)
     # 同时进行向量重检索的结果的返回 vec_re_search
# 对于向量重检索分析
        相当于应用：vec_re_search
"""

"""
对于分析系统的状态，可以使用监听者模式制作一个动作触发器（回调函数触发器（自动提单、自动回调给用户结论【这里应该写一个接口让用户给出回调地址才对】），结论落库触发器）
对于数据库的插入和查询的原则：
    1、永远接收批量数据的upsert操作
    2、也永远支持批量查询的动作
"""


class LogAnalysis:
    """日志分析模型的父类"""

    @property
    async def get_result(self, log_id):
        """用于获取模型的分析结果"""
        pass

    async def run(self, log_id):
        """
        用于执行模型的分析过程
        """
        pass

    async def trigger(self):
        """主要用于触发特殊的动作"""
        pass


class ExpertLogAnalysis(LogAnalysis):
    """
    专家经验的日志分析模型过程
    """

    async def get_result(self, log_id):
        """用于获取模型的分析结果"""
        pass

    async def run(self, log_id):
        """
        用于执行模型的分析过程  
        """
        pass

    async def trigger(self):
        """
        用于触发自动提单功能
        用于触发落库的动作(这里可是要包含两部分的落库：errmsg的落库和专家推理结果的落库)
        """
        pass


class VectorLogAnalysis(LogAnalysis):
    """
    向量检索分析模型过程
    """

    async def get_result(self, log_id):
        """用于获取模型的分析结果"""
        pass

    async def run(self, log_id):
        """
        用于执行模型的分析过程
        """
        pass

    async def trigger(self):
        """
        用于触发分析结果的落库动作，
        用于触发检索历史的落库动作
        """
        pass


class FullInference(LogAnalysis):  # 这里应该考虑责任链模式来实现这个过程
    """
    主要用于ai智能日志分析的全量过程,包含专家推理和向量检索
    """

    def __init__(self, log_id, tdb_link):
        self.log_id = log_id
        self.tdb_link = tdb_link

    async def run(self):
        """
        用于执行全量模型的分析过程,即调用两个子流程
        """
        pass

    async def trigger(self, callback):
        """
        用于触发用户的回调动作，
        """
        pass


class ManageDBData:
    async def batch_upsert(self, data):
        """
        用于批量更新或插入数据库数据
        """
        pass

    async def batch_query(self, data):
        """
        用于批量查询数据库数据
        """
        pass


class ManageErrmsgDBData(ManageDBData):
    async def batch_upsert(self, data):
        """
        用于批量更新或插入errmsg数据库数据
        """
        pass

    async def batch_query(self, data):
        """
        用于批量查询errmsg数据库数据
        """
        pass


class ManageExpertInferenceDBData(ManageDBData):
    async def batch_upsert(self, data):
        """
        用于批量更新或插入专家数据库数据
        """
        pass

    async def batch_query(self, data):
        """
        用于批量查询专家数据库数据
        """
        pass


class ManageVecDBData(ManageDBData):
    async def batch_upsert(self, data):
        """
        用于批量更新或插入向量数据库数据
        """
        pass

    async def batch_query(self, data):
        """
        用于批量查询向量数据库数据
        """
        pass


class ManageVecSearchLogDBData(ManageDBData):
    async def batch_upsert(self, data):
        """
        用于批量更新或插入推理数据库数据
        """
        pass

    async def batch_query(self, data):
        """
        用于批量查询推理数据库数据
        """
        pass

    # 知识库的更新机制，1、每一天都要进行数据库的插入动作 2、每一天都要将最近一次检索时间跨度大于6个月且总检索次数小于5的数据删掉
