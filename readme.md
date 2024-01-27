[![Run Tests](https://github.com/WalliedeWalrus/farm/actions/workflows/run-tests.yml/badge.svg)](https://github.com/WalliedeWalrus/farm/actions/workflows/run-tests.yml)

# Contineous Deployment with Github Actions, Flask and Digital Ocean Droplet

This assignment was not just a walk in the park... I ran into a lot of errors that had to be investigated by a lot of reading. In the end I succeededto fix the problems but I'm glad the job is done. Though I learned a lot during the process.

After running the droplet I had a hard time with GitHub Actions and combining it with the automated SSH authorisation. I tried to tackle this step by step but at some point although following the advised steps it simply wouldn't work. So I started from scratch with a new droplet and new repository. This time it worked like it should.

I registered 3 secrets ssh_username ssh_key and ssh_host

After that I was able to run scripts on my Droplet. I first checked simple things to see if it worked. When it seemed to be working properly I tried to pull my git with the pull git command. Here I got stuck with a fatal error (no git repository)

I found out I had to initiate git by cloning the repository to the droplet and after that the git pull worked. I had to play around with file structure, nginx, farm.service etc but in the end it all worked fine.

I added the little website to test if all changes ended up working in the droplet. And I was very happy it did. It cost me days and my normal work is quite busy so I was really tired and glad I can now finish the Back end development course just in time.

Thanks for the Back end development journey
