import os,sys
import utils
from base.Loadable import Loadable

class ExperienceDataset(Loadable):
    ''' Class used to store data from runs with a learning agent'''
    def __init__(self, name='Experience', filename_prefix=None, filename=None):
        self.name = name
        self.time_stamps = []
        self.states = []
        self.actions = []
        self.immediate_cost = []
        self.policy_parameters = []
        self.curr_episode = -1
        self.state_changed = True
        if filename is not None:
            self.filename=filename
        else:
            self.filename = self.name+'_dataset' if filename_prefix is None else filename_prefix+'_dataset'
            utils.print_with_stamp('Initialising new experience dataset',self.name)
        
        Loadable.__init__(self,name=name,filename=self.filename)

        # if a filename was passed, try loading it
        if filename is not None:
            self.load()

        self.register_types([list])
        self.register(['curr_episode'])

    def add_sample(self,t,x_t=None,u_t=None,c_t=None, policy_parameters=None):
        curr_episode = self.curr_episode
        self.time_stamps[curr_episode].append(t)
        self.states[curr_episode].append(x_t)
        self.actions[curr_episode].append(u_t)
        self.immediate_cost[curr_episode].append(c_t)
        self.state_changed = True

    def new_episode(self, policy_params=None):
        self.time_stamps.append([])
        self.states.append([])
        self.actions.append([])
        self.immediate_cost.append([])
        if policy_params:
            self.policy_parameters.append(policy_params)
        else:
            self.policy_parameters.append([])

        self.curr_episode += 1
        self.state_changed = True

    def n_samples(self):
        ''' Returns the total number of samples in this dataset '''
        return sum([len(s) for s in self.states])

    def n_episodes(self):
        ''' Returns the total number of episodes in this dataset '''
        return len(self.states)

    def reset(self):
        utils.print_with_stamp('Resetting experience dataset (WARNING: data from %s will be overwritten)'%(self.filename),self.name)
        self.time_stamps = []
        self.states = []
        self.actions = []
        self.immediate_cost = []
        self.policy_parameters = []
        self.curr_episode = -1
        self.state_changed = False # Let's give people a last chance of recovering their data. Also, we don't want to save an empty experience dataset

    def truncate(self, episode):
        ''' Resets the experience to start from the given episode number'''
        if episode <= self.currernt_episode and episode > 0:
            utils.print_with_stamp('Resetting experience dataset to episode %d (WARNING: data from %s will be overwritten)'%(episode,self.filename),self.name)
            self.current_episode  = episode
            self.time_stamps = self.time_stamps[:episode]
            self.states = self.states[:episode]
            self.actions = self.actions[:episode]
            self.immediate_cost = self.immediate_cost[:episode]
            self.policy_parameters = self.policy_parameters[:episode]
            self.state_changed = True
