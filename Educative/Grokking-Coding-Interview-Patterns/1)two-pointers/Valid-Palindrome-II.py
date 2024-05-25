def is_palindrome(s):
  l, r = 0, len(s) - 1
  while l < r:
    if s[l] != s[r]:
      delete_l_str = s[l+1:r+1] # excluding lth index
      delete_r_str = s[l:r] # excluding rth index
      return delete_l_str == delete_l_str[::-1] or delete_r_str == delete_r_str[::-1]
    l, r = l+1, r-1
  
  return True