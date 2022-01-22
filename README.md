# 筆記

## 常見注意事項

1. python 中以 `list` 初始化二維陣列
    - 錯誤方式
        - `[[v]*n]*m`，每個子列 `[v]*n` 接指向同樣記憶體
    - 正確方式
        - `[[v]*n for _ in range(m)]`

## 題解

### 57. Insert Interval

1. 以 `bisect.bisect` 找出新插入值 `newInterval` 的 `start` 於 `intervals` 中位於的位置 `idx`
2. 判斷 `intervals[idx: ]` 中有多少 elements 的起始值 `start_i` 小於 `newInterval` 的 `end，`
    - 避免使用的索引 `overlap_idx` 超出 `intervals` 的數量，
    - 紀錄由 `idx` 算起需要被移除的 elements 數量 `remove_cnt`
    - 當 `intervals[overlap_idx]` 的 `end_overlap_idx` 大於等於 `newInterval` 的 `end` 時，結束判斷，並記錄新插入區間的結尾值 `end_overlap_idx`
3. 當插入位置 `idx` 不為第一個時，檢查前一個 element，`intervals[idx - 1]`，的 `end` 是否大於等於 `newInterval` 的 `start`
    - 成立的話新插入的起始值更新為 `intervals[idx - 1]` 的 `start`
        - **判斷 `intervals[idx - 1]` 的 `end` 是否大於 `newInterval` 的 `end`**
            - 成立的話新插入的結尾值更新為 `intervals[idx - 1]` 的 `end`
        - 刪除 `intervals` 中由 `idx` 算起的 `remove_cnt` 個 element，以及第 `idx-1` 個 element
        - 在 `idx-1` 的位置插入新 element
    - 不成立的話刪除 `intervals` 中由 `idx` 算起的 `remove_cnt` 個 element，並在 `idx` 的位置插入新 element

### 224.Basic Calculator

1. 依序判斷進來的字元為數字、運算子或括號
    - 如為數字，先暫存其值，等遇到運算子或括號時再進行處理
    - 如為運算子，則計算在其之前的運算式
        - 當前累計的計算結果為 l-value，暫存的值為 r-value，暫存的運算子為 r-value 的正負號
        - 計算後將暫存的運算子更新為當前的運算子，暫存的值歸零
    - 如為左括號，將當前計算結果及暫存的運算子存入 stack，並初始化當前計算結果與暫存的運算子
    - 如為右括號，計算在其之前的運算式
        - 將結果做為 r-value，並取出 stack 最上層的運算子和先前結果，計算出當前結果值
2. 以累計結果、暫存值、暫存運算子計算最後結果，再將暫存的值歸零

### 413. Arithmetic Slices

1. 由最後三個 element 開始，判斷前兩項的差值是否等於後兩項的差值
    - 成立的話則紀錄以第一項的索引為首，連續三個 element 為等差數列，數量為 1
        - 查詢以第二項的索引為首時，是否亦有等差數列，成立的話更新以第一項的索引為首的等差數列的數量
2. 累加以每個 element 為首時的等差數列的數量

### 446. Arithmetic Slices II - Subsequence

1. 以 DP 的方式規劃，先記錄數列 `nums` 中的任意兩值，`nums[i]` 及 `nums[j]`，是否存在第三值 `nums[k]`，使其成為等差子數列，其中 `k>j>i`
    - **不要對輸入數列 `nums` 做排序**
    - 對於一組 `nums[i]` 及 `nums[j]`，`k` 可能不只一種
    - 分別記錄間格 `spacing`、`k` 的值 `index` 以及數量 `counter`
2. 從可能的索引最大值開始判斷，是否存在以 `nums[i]` 及 `nums[j]` 起始，長度大於 3 的等差子數列
    - 成立的話，更新以 `nums[i]` 及 `nums[j]` 起始的等差子數列的數量 `counter`
3. 累加以數列 `nums` 中的任意兩值，`nums[i]` 及 `nums[j]` 起始的等差子數列的數量
