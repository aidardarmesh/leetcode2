/**
 * @param {number[][]} points
 * @param {number} K
 * @return {number[][]}
 */
var kClosest = function(points, K) {
    let origins = [0,0];
    
    let newPoints = points.sort((A, B) => {
        distA = Math.sqrt((A[0]-origins[0])**2 + (A[1]-origins[1])**2)
        distB = Math.sqrt((B[0]-origins[0])**2 + (B[1]-origins[1])**2)
        return distA - distB;
    })
    
    return newPoints.splice(0, K);
};
