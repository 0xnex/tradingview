//@version=6
indicator("多重EMA系统(高低收) - 首个关键K线识别", overlay=true)

// 输入参数
emaLength = input.int(32, title="EMA长度", minval=1)
showLabels = input(true, "显示关键K线标识")
useTable = input(true, "使用表格显示EMA值")

// 计算三个不同价格源的EMA
emaHigh = ta.ema(high, emaLength)    // 最高价EMA
emaLow = ta.ema(low, emaLength)      // 最低价EMA
emaClose = ta.ema(close, emaLength)  // 收盘价EMA

// 定义EMA通道状态
channelUp = emaHigh > emaHigh[1] and emaLow > emaLow[1] and emaClose > emaClose[1]
channelDown = emaHigh < emaHigh[1] and emaLow < emaLow[1] and emaClose < emaClose[1]

// 关键K线条件
bullishKeyK = channelUp and (close > emaHigh) and (close[1] <= emaHigh[1])
bearishKeyK = channelDown and (close < emaLow) and (close[1] >= emaLow[1])

// 跟踪通道状态变化
var bool lastChannelUp = false
var bool lastChannelDown = false
var bool markedFirstKeyK = false

// 检测通道状态变化
channelChanged = (channelUp and not lastChannelUp) or (channelDown and not lastChannelDown)

// 重置标记状态当通道变化时
if channelChanged
    markedFirstKeyK := false
    lastChannelUp := channelUp
    lastChannelDown := channelDown

// 绘制三条EMA线
plot(emaHigh, "EMA(最高价)", color=color.rgb(255, 0, 0), linewidth=1)
plot(emaLow, "EMA(最低价)", color=color.rgb(0, 0, 255), linewidth=1)
plot(emaClose, "EMA(收盘价)", color=color.rgb(0, 255, 0), linewidth=1)

// 标记首个关键K线
if showLabels and not markedFirstKeyK
    if bullishKeyK
        label.new(bar_index, low, "首↑", style=label.style_label_up, 
                 color=color.new(color.green, 70), textcolor=color.white, 
                 size=size.normal, yloc=yloc.belowbar)
        markedFirstKeyK := true
    else if bearishKeyK
        label.new(bar_index, high, "首↓", style=label.style_label_down, 
                 color=color.new(color.red, 70), textcolor=color.white, 
                 size=size.normal, yloc=yloc.abovebar)
        markedFirstKeyK := true

// 在图表右侧显示当前EMA值
if useTable and barstate.islast
    var table emaTable = table.new(position.top_right, 1, 4, 
                                 bgcolor=color.new(color.gray, 90))
    table.cell(emaTable, 0, 0, "通道状态: " + 
              (channelUp ? "上涨" : channelDown ? "下跌" : "震荡"), 
              text_color=color.white)
    table.cell(emaTable, 0, 1, "EMA(高): " + str.tostring(emaHigh, format.mintick), 
              text_color=color.white)
    table.cell(emaTable, 0, 2, "EMA(低): " + str.tostring(emaLow, format.mintick), 
              text_color=color.white)
    table.cell(emaTable, 0, 3, "EMA(收): " + str.tostring(emaClose, format.mintick), 
              text_color=color.white)
