if not x%GITHUB_USER_NAME% == x (
	git config user.name "%GITHUB_USER_NAME%
)
if not x%GITHUB_EMAIL% == x (
	git config user.email %GITHUB_EMAIL%
)
git config credential.helper wincred
