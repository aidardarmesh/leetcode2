/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    var n = s.length, ans = '';
    const LEFT = 0, RIGHT = 1;
    
    for (let i = 0; i < n; i++) {
        let bounds = getBoundaries(s, i, i);
        if (bounds[RIGHT] - bounds[LEFT] + 1 > ans.length) {
            ans = s.slice(bounds[LEFT], bounds[RIGHT]+1);
        }
        
        if (i+1 < n) {
            let bounds = getBoundaries(s, i, i+1);
            if (bounds[RIGHT] - bounds[LEFT] + 1 > ans.length) {
                ans = s.slice(bounds[LEFT], bounds[RIGHT]+1);
            }
        }
    }
    
    return ans;
};

var getBoundaries = function(s, left, right) {
    while (left >= 0 && right < s.length && s[left] == s[right]) {
        left -= 1;
        right += 1;
    }
    
    return [left+1, right-1];
};
