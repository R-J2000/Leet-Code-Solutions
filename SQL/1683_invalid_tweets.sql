# 1683 Invalid Tweets

/*
Solution 1 (Most Intuitive)
Intuition and Approach
- Use the SELECT and FROM keywords to pick tweet_id column from Tweets table.
- Use WHERE keyword to filter tweets based on length. This can be done using the LENGTH function.
*/
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
