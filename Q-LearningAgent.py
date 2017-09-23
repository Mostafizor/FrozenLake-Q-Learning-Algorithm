import gym
import numpy as np

# Q-Learning ALgorithm
class Q_Learning(object):
	def __init__(self):
		self.lr = 0.8 # Learning Rate
		self.y = 0.95 # Discounting Factor
		self.Qt = np.zeros([env.observation_space.n, env.action_space.n]) # Initialise Q-Value Table

	def select_action(self, observation):
		return np.argmax(self.Qt[observation] + np.random.randn(1, env.action_space.n)*(1./(e+1))) # Choose an action by greedily (with noise) picking from Q table. Noise ensures that the agent takes random actions in the exploration stage.

	def new_Q(self, R, Q):
		return R + self.y*Q # Calculate New Q-Value After Taking Action

	def update_Q(self, Qnew):
		self.Qt[s,a] = self.Qt[s,a] + self.lr*(Qnew - self.Qt[s,a]) # Update Q-Value Using Bellman Equation

# Create The Environment
env = gym.make('FrozenLake-v0')
num_episodes = 10000

# Create The Agent
agent = Q_Learning()

# Agent-Environment Training Loop
rList = [] # List of Rewards Per Episode
wList = [] # List of Last 100 Rewards. Win Condition: Average Of Last 100 Rewards >= 0.78.
sList = [] # List of Steps
print('Agent Is Training...')
for e in range(1, num_episodes+1):
	observation = env.reset() # Get First Observation
	steps = 0
	score = 0
	while steps < 99:
		s = observation
		a = agent.select_action(observation)
		observation, reward, done, info = env.step(a)
		Qnew = agent.new_Q(reward, np.amax(agent.Qt[observation]))
		agent.update_Q(Qnew)
		score += reward
		if done:
			break
	rList.append(score)
	wList.append(score)
	sList.append(steps)
	if e in range(0, num_episodes+1, 100):
			score = sum(wList)/100
			if score >= 0.78:
				print('Q-Table: ')
				print(agent.Qt)
				print('Agent Has Successfully Completed The Environment!')
				print('Number of Episodes before Completion: %s' %(e))
				break
			elif e == num_episodes:
				print('Agent Failed To Complete The Environment :(')
				print('Average Score of Last 100 Episodes: %s' %(sum(wList)/100))
			else:
				wList = []
				continue

# Evaluate The Agent By Playing And Rendering One Last Episode
evaluate = raw_input('Would you like to evaluate the agent? [Y/N] > ').upper()
if evaluate == 'Y':
	observation = env.reset()
	steps = 0
	while steps < 99:
		env.render()
		steps += 1
		a = agent.select_action(observation)
		observation, reward, done, info = env.step(a)
		if done:
			env.render()
			break
else:
	pass



