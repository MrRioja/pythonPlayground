// Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
// Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
// She tabulates the number of times she breaks her season record for most points and least points in a game.
// Points scored in the first game establish her record for the season, and she begins counting from there.
// Example:
// scores = [12,24,10,24]
// Scores are in the same order as the games played. She tabulates her results as follows:
//                                  Count
// Game  Score  Minimum  Maximum   Min Max
// 0      12     12       12       0   0
// 1      24     12       24       0   1
// 2      10     10       24       1   1
// 3      24     10       24       1   1
// Given the scores for a season, determine the number of times Maria breaks her records for most and least points
// scored during the season.

function breakingRecords(scores) {
  let min_score = [0, scores[0]];
  let max_score = [0, scores[0]];

  for (const score of scores) {
    if (score > max_score[1]) {
      max_score[0] += 1;
      max_score[1] = score;
    }
    if (score < min_score[1]) {
      min_score[0] += 1;
      min_score[1] = score;
    }
  }

  console.log(max_score[0], min_score[0]);
}

const scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42];

breakingRecords(scores);
