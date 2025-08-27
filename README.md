记录在bilibili和youtube上发现的指标

# EMA高低收通道
[原始视频](https://www.bilibili.com/video/BV1hF4m1T73E?spm_id_from=333.788.recommend_more_video.4&vd_source=7fc5922397de9362d6f5bfc73e707c59)
[代码](https://github.com/0xnex/tradingview/blob/main/ema_hlc_channel.pine)

- 📈买入规则一：价格从下方穿过移动平均区域，表示趋势可能转向牛市
- 📉买入规则二：价格保持在移动平均区域内，偶尔突破但不收盘在区域外
- 💼买入规则三：价格带有动能突破区域，利用蜡烛图形态识别
- 💰买入策略：设置止损，利润目标为一比一和一比二，无风险交易
- 📉卖出规则一：价格从上方穿过移动平均线，留下空隙
- 📈卖出规则二和规则三：价格回调至移动平均区域内，三种有效价格走势
- 📉卖出策略：利润目标及止损设置，避免止损位太远时进入交易

# ARH999  DCA
[code]((https://github.com/0xnex/tradingview/blob/main/ahr999.pine))
This indicator implements the AHR999-based Dollar-Cost Averaging (DCA) investment strategy for Bitcoin.
* Buy rules (T+1 execution):
  * Invest $200 per day when AHR999 < 0.45 (deep undervaluation).
  * Invest $50 per day when 0.45 ≤ AHR999 < 1.2 (fair value zone).
* Sell rule:
  * When AHR999 > 4 (strong overvaluation), sell all holdings (reset).
* Visualization:
  * Orange line → cumulative invested cost.
  * Blue line → current portfolio value (based on BTC price).

This lets you see how a systematic DCA plan based on AHR999 would perform over time, without displaying every individual trade.
