/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var res = 0;
    var seen = {};
    var last_rep_id = -1;
    
    for (let i = 0; i < s.length; i++) {
        if (seen[s[i]] !== undefined) {
            last_rep_id = Math.max(last_rep_id, seen[s[i]]);
        }
        seen[s[i]] = i;
        res = Math.max(res, i - last_rep_id);
    }
    return res;
};
