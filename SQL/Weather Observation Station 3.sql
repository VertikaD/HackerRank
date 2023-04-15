SELECT DISTINCT City
FROM Station
WHERE MOD(ID,2) = 0 -- even when remainder of division of a number by 2 is 0


-- MOD() function returns the remainder of a number divided by another number. 
