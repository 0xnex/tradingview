//@version=6
indicator("EMA Channel Key K-Lines", overlay=true)

// Input parameters
emaLength = input.int(32, title="EMA Length", minval=1)

// Calculate three EMAs
emaHigh = ta.ema(high, emaLength)
emaLow = ta.ema(low, emaLength)
emaClose = ta.ema(close, emaLength)

// Plot EMAs
plot(emaHigh, "High EMA", color=color.red)
plot(emaLow, "Low EMA", color=color.blue)
plot(emaClose, "Close EMA", color=color.green)

// Channel calculations
channelHeight = emaHigh - emaLow
bodySize = math.abs(close - open)
totalRange = high - low
bodyRatio = bodySize / totalRange

// Track last signal direction
var bool lastWasBuy = false
var bool lastWasSell = false

// Key Buy K-line conditions:
// 1. Close above channel high
// 2. K-line height >= channel height
// 3. Body size >= 2/3 of total range
// 4. Not immediately after another buy signal
keyBuyCondition = close > emaHigh and 
                 (high - low) >= channelHeight and 
                 bodyRatio >= 0.66 and
                 not lastWasBuy

// Key Sell K-line conditions:
// 1. Close below channel low
// 2. K-line height >= channel height
// 3. Body size >= 2/3 of total range
// 4. Not immediately after another sell signal
keySellCondition = close < emaLow and 
                  (high - low) >= channelHeight and 
                  bodyRatio >= 0.66 and
                  not lastWasSell

// Mark key K-lines
if keyBuyCondition
    label.new(bar_index, low, "BUY", color=color.green, style=label.style_label_up, textcolor=color.white, yloc=yloc.belowbar)
    lastWasBuy := true
    lastWasSell := false
    
if keySellCondition
    label.new(bar_index, high, "SELL", color=color.red, style=label.style_label_down, textcolor=color.white, yloc=yloc.abovebar)
    lastWasSell := true
    lastWasBuy := false

// Background color for channel
fill(plot(emaHigh, display=display.none), plot(emaLow, display=display.none), color=color.new(color.gray, 90))
