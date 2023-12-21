/*
 * ❗️❗️ 필독 ❗️❗️
 * - 함수 블록 내부에만 작성해주세요.
 * - 결과값을 return 하세요.
 * - 추가적인 test가 필요한 경우에는 기존 test 코드 밑에 추가해주세요.
 * - 코드 실행 시 모든 테스트가 true인 경우 통과입니다!
 */

/*   문제 출제
 *
 *   🍬 사탕 나누기
 * - A가 가지고 있는 candies를 N명의 friends에게 공평하게 나누어 줄 때,
 * - 각 friends가 가져갈 수 있는 candies의 개수를 구하는 함수를 작성하세요.
 *
 * ❗️ 제한 조건 ❗️
 * - 입력되는 수는 양의 정수입니다.
 * - 반환되는 값은 정수로 나와야 합니다.
 *
 */

function question(candies, friends) {
  // 여기에서 코드 작성해주세요!

  let result = Math.floor(candies / friends); // 각 n명이 가져갈 수 있는 캔디

  return result;
}

// 여기는 결과값 함수이므로 신경쓰지 않으셔도 됩니다!
Test(
  question,
  [
    [32, 6],
    [56, 4],
    [34, 5],
    [73, 6],
    [23, 3],
    [45, 7],
    [89, 8],
    [73, 9],
  ],
  [5, 14, 6, 12, 7, 6, 11, 8]
);

function Test(question, conditions, results) {
  for (let index in results) {
    const result = question(...conditions[index]) === results[index];
    console.log(`테스트 ${+index + 1}`, result);
    if (!result) {
      console.log("테스트에 통과하지 못했습니다.");
      return;
    }
  }

  console.log("테스트에 통과하셨습니다!");
}
