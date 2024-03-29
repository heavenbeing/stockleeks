#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import akshare as ak
import libs.common as common

print(ak.__version__)

# 历史行情数据
# 日频率
# 接口: stock_zh_a_daily
# 目标地址: https://finance.sina.com.cn/realstock/company/sh600006/nc.shtml(示例)
# 描述: A 股数据是从新浪财经获取的数据, 历史数据按日频率更新; 注意其中的 sh689009 为 CDR, 请 通过 stock_zh_a_cdr_daily 接口获取
# 限量: 单次返回指定 A 股上市公司指定日期间的历史行情日频率数据
# adjust=""; 默认为空: 返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据;
# 二、不复权、前复权、后复权的用途
# 不复权的话，K线图能真实反应股价历史的除权信息，缺点是会留有大缺口，均线系统被打乱。
# 前复权以目前价为基准复权，可以很清楚的看到成本分布情况，如相对最高、最低价，成本密集区域，以及目前股价所处的位置是高还是低。如果进行技术分析，最好用前复权，这样当前的价格是最新的实际价格，且K线均线的走势是连续性的，不影响看盘。
# 后复权保持上市第一天的价格不变，根据分红配股数据处理之后的价格，这会导致最后一天的价格显示出来不是实际成交价，但可以看出股票真实价值的增加及持股者的真实收益率。如果进行价值投资，建议采用后复权，这样计算的收益率是相对正确的，查询也比较直观。
# 三、总结
# 综上所述，前复权可以实现技术指标的连续性，后复权可以实现股价走势的连续性，不复权则可以直观显示出股价除权除息后是填权还是贴权的走势

stock_zh_a_daily_qfq_df = ak.stock_zh_a_daily(symbol="sz000002", adjust="")
print(stock_zh_a_daily_qfq_df)

stock_zh_a_daily_qfq_df = ak.stock_zh_a_daily(symbol="sz000002", start_date="20200101", end_date="20210101", adjust="")
print(stock_zh_a_daily_qfq_df)

# 插入到 MySQL 数据库中
common.insert_db(stock_zh_a_daily_qfq_df, "stock_zh_a_daily", True, "`symbol`")



