/*
문제 설명
정수 배열 arr가 주어집니다.
다음 작업을 수행하는 함수를 작성하세요:

배열 요소 각각에 2를 곱한 새 배열을 만든다. (map 활용)

새 배열에서 5 이상인 수만 필터링한다. (filter 활용)

필터링된 수들의 합을 구한다. (reduce 활용)

결과로 필터링된 수들의 합을 반환하세요.
*/



const arr1 = [1, 2, 3, 4]
const arr2 = [0, 1, 2]
const arr3 = [3, 4, 5]

const arr4 = arr1.map((x) => x * 2);
console.log(arr4);
const arr5 = arr3.filter((x) => x >= 5);
console.log(arr5);

const sumWithInitial = arr3.reduce((now, a) => now + a, 0);
console.log(sumWithInitial);

const nums = [1, 2, 3, 4, 5];
console.log(nums.reduce((now, a) => now + a, 0));
const nums2 = [5, 2, 7, 1, 9];
console.log(nums2.reduce((acc, cur) => cur > acc ? cur : acc ));

