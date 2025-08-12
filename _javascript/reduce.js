const arr = [1, 2, 3, 4, 5]
console.log(arr.reduce((acc, cur) => acc + cur, 0))

const str = "banana"
const strArr = str.split('');
const frequencyMap = strArr.reduce((acc, cur) => {
    acc[cur] = (acc[cur] || 0) + 1;
    return acc;
}, {})
console.log(frequencyMap)
const sorted = Object.entries(frequencyMap).sort((a, b) => {
    if (b[1] === a[1]) {
      return a[0].localeCompare(b[0]); // 알파벳 오름차순
    }
    return b[1] - a[1]; // 빈도 내림차순
});

console.log(sorted[0][0]);

const nested = [[1, 2], [3, 4], [5]];
const flattened = nested.reduce((acc, cur) => acc.concat(cur), []);
console.log(flattened);