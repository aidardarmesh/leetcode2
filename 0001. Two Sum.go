func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    
    for i, num := range nums {
        num2 := target - num
        i2, ok := m[num2]
        
        if ok {
            return []int{i, i2}
        } else {
            m[num] = i
        }
    }
    
    return []int{-1, -1}
}
