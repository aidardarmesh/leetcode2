/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var l3 = new ListNode(-1);
    var head = l3;
    var sum = 0;
    var carry = 0;
    
    while (l1 !== null && l2 !== null) {
        sum = l1.val + l2.val + carry;
        l3.next = new ListNode(sum % 10);
        carry = Math.floor(sum / 10);
        l1 = l1.next;
        l2 = l2.next;
        l3 = l3.next;
    }
    
    while (l1 !== null) {
        sum = l1.val + carry;
        l3.next = new ListNode(sum % 10);
        carry = Math.floor(sum / 10);
        l1 = l1.next;
        l3 = l3.next;
    }
    
    while (l2 !== null) {
        sum = l2.val + carry
        l3.next = new ListNode(sum % 10);
        carry = Math.floor(sum / 10);
        l2 = l2.next;
        l3 = l3.next;
    }
    
    if (carry !== 0) {
        l3.next = new ListNode(carry);
    }
    
    return head.next;
};
