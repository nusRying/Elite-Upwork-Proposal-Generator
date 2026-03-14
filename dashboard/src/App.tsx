import { useState, useEffect } from 'react'
import { Send, Zap, Shield, FileText, ChevronRight, BarChart3, Clock, Sparkles, Plus, Trash2, X, Edit2 } from 'lucide-react'
import { motion, AnimatePresence } from 'framer-motion'

export default function App() {
  const [jobDesc, setJobDesc] = useState('')
  const [isGenerating, setIsGenerating] = useState(false)
  const [proposal, setProposal] = useState<any>(null)
  const [activeTab, setActiveTab] = useState('generator')
  const [activeCategory, setActiveCategory] = useState('All')

  const [portfolioItems, setPortfolioItems] = useState([
    {
      id: 1,
      title: "Autonomous SaaS Sales Agent",
      category: "AI",
      metrics: "$12k+ Revenue Generated",
      link: "https://portfolio.example.com/saas-agent",
      desc: "Multi-agent LangGraph system that automates lead nurturing and closing."
    },
    {
      id: 2,
      title: "Enterprise Data Pipeline",
      category: "Automation",
      metrics: "99.9% Reliability",
      link: "https://portfolio.example.com/data-pipeline",
      desc: "Robust ETL pipeline using Python and Airflow for 1TB+ weekly data."
    },
    {
      id: 3,
      title: "Elite Web Dashboard",
      category: "Web",
      metrics: "Sub-100ms Latency",
      link: "https://portfolio.example.com/dashboard",
      desc: "Modern React/Next.js interface with real-time hardware monitoring."
    },
    {
      id: 4,
      title: "Custom LLM Integrator",
      category: "AI",
      metrics: "3.5B Parameters Optimized",
      link: "https://portfolio.example.com/llm-integrator",
      desc: "Local inference engine using Ollama for secure corporate workflows."
    },
    {
      id: 5,
      title: "E-commerce Optimizer",
      category: "Web",
      metrics: "40% Conversion Lift",
      link: "https://portfolio.example.com/ecommerce",
      desc: "A/B testing and pixel-perfect UI overhaul for a high-traffic shop."
    },
    {
      id: 6,
      title: "Social Media Automator",
      category: "Automation",
      metrics: "20h/week Saved",
      link: "https://portfolio.example.com/social-auto",
      desc: "Cross-platform posting and engagement engine using Zapier and custom APIs."
    }
  ])

  const [isAdding, setIsAdding] = useState(false)
  const [editId, setEditId] = useState<number | null>(null)
  const [newProject, setNewProject] = useState({ title: '', category: 'AI', metrics: '', link: '', desc: '' })

  const handleAddProject = () => {
    if (!newProject.title) return
    
    if (editId !== null) {
      setPortfolioItems(portfolioItems.map(p => p.id === editId ? { ...newProject, id: editId } : p))
      setEditId(null)
    } else {
      const id = portfolioItems.length > 0 ? Math.max(...portfolioItems.map(i => i.id)) + 1 : 1
      setPortfolioItems([...portfolioItems, { ...newProject, id }])
    }
    
    setIsAdding(false)
    setNewProject({ title: '', category: 'AI', metrics: '', link: '', desc: '' })
  }

  const handleEdit = (project: any) => {
    setNewProject({ ...project })
    setEditId(project.id)
    setIsAdding(true)
  }

  const handleDeleteProject = (id: number) => {
    setPortfolioItems(portfolioItems.filter(p => p.id !== id))
  }

  const filteredPortfolio = activeCategory === 'All' 
    ? portfolioItems 
    : portfolioItems.filter(item => item.category === activeCategory)

  const [copied, setCopied] = useState(false)

  const handleCopy = () => {
    if (!proposal) return
    navigator.clipboard.writeText(proposal.proposal.draft)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  const [knowledgeItems, setKnowledgeItems] = useState<any[]>([])
  
  const fetchKnowledge = async () => {
    try {
      const response = await fetch('/api/knowledge')
      const data = await response.json()
      setKnowledgeItems(data.items || [])
    } catch (error) {
      console.error('Failed to fetch knowledge', error)
    }
  }

  useEffect(() => {
    if (activeTab === 'knowledge') {
      fetchKnowledge()
    }
  }, [activeTab])

  const handleUpdateStatus = async (proposalId: number, status: string) => {
    try {
      await fetch('/api/proposals/status', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ proposal_id: proposalId, status })
      })
      setProposal({ ...proposal, status_updated: true })
    } catch (error) {
      console.error('Failed to update status', error)
    }
  }

  const handleDeleteKnowledge = async (id: number) => {
    try {
      await fetch(`/api/knowledge/${id}`, { method: 'DELETE' })
      fetchKnowledge()
    } catch (error) {
      console.error('Failed to delete knowledge', error)
    }
  }

  const handleGenerate = async () => {
    setIsGenerating(true)
    setCopied(false)
    try {
      const response = await fetch('/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ job_description: jobDesc })
      })
      const data = await response.json()
      setProposal(data)
    } catch (error) {
      console.error('Generation failed', error)
    } finally {
      setIsGenerating(false)
    }
  }

  return (
    <div className="min-h-screen p-8 max-w-7xl mx-auto">
      <header className="flex justify-between items-center mb-12">
        <div>
          <h1 className="text-4xl font-bold bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent glow-text uppercase tracking-tighter text-glow">
            Elite Proposal Assistant
          </h1>
          <p className="text-gray-400 mt-2">Unbeatable Upwork Proposals via Local LLM Chain</p>
        </div>
        <div className="flex gap-4">
          <button 
            onClick={() => setActiveTab('generator')}
            className={`px-4 py-2 rounded-full transition-all ${activeTab === 'generator' ? 'bg-primary text-white shadow-lg shadow-primary/20' : 'text-gray-400 hover:text-white'}`}
          >
            Generator
          </button>
          <button 
            onClick={() => setActiveTab('knowledge')}
            className={`px-4 py-2 rounded-full transition-all ${activeTab === 'knowledge' ? 'bg-primary text-white shadow-lg shadow-primary/20' : 'text-gray-400 hover:text-white'}`}
          >
            Knowledge
          </button>
          <button 
            onClick={() => setActiveTab('portfolio')}
            className={`px-4 py-2 rounded-full transition-all ${activeTab === 'portfolio' ? 'bg-primary text-white' : 'text-gray-400 hover:text-white'}`}
          >
            Portfolio
          </button>
        </div>
      </header>

      <main>
        {activeTab === 'generator' && (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <section className="space-y-6">
              <div className="glass-card p-8 rounded-3xl">
                <div className="flex justify-between items-center mb-6">
                  <label className="text-[10px] font-bold text-gray-500 uppercase tracking-[0.2em] flex items-center gap-2">
                    <FileText size={14} className="text-primary" /> Input / Job Description
                  </label>
                  <div className="flex items-center gap-2 text-[10px] font-medium text-gray-600">
                    <Clock size={12} /> Auto-saving enabled
                  </div>
                </div>
                <textarea 
                  className="w-full h-96 bg-black/20 border border-white/5 rounded-2xl p-6 text-gray-300 focus:outline-none focus:border-primary/40 transition-all resize-none mb-6 placeholder:text-gray-700 leading-relaxed"
                  placeholder="Paste the job requirements here to begin the synthesis..."
                  value={jobDesc}
                  onChange={(e) => setJobDesc(e.target.value)}
                />
                <button 
                  onClick={handleGenerate}
                  disabled={isGenerating || !jobDesc}
                  className={`w-full py-4 rounded-xl flex items-center justify-center gap-3 font-bold tracking-tight transition-all active:scale-[0.98] ${isGenerating ? 'bg-gray-800 text-gray-500 cursor-not-allowed' : 'bg-white text-black hover:bg-primary hover:text-white glow-primary'}`}
                >
                  {isGenerating ? (
                    <>
                      <Zap size={20} className="animate-pulse" />
                      ORCHESTRATING AGENTS...
                    </>
                  ) : (
                    <>
                      <Zap size={20} />
                      GENERATE ELITE PROPOSAL
                    </>
                  )}
                </button>
              </div>
            </section>

            <section className="space-y-6">
              <AnimatePresence mode="wait">
                {proposal ? (
                  <motion.div 
                    key="results"
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -20 }}
                    className="glass-card p-8 rounded-3xl h-full border-primary/20"
                  >
                    <div className="flex justify-between items-center mb-8">
                      <div className="flex items-center gap-4">
                        <div className="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center border border-primary/20">
                          <Zap size={20} className="text-primary" />
                        </div>
                        <div>
                          <h3 className="text-sm font-bold text-white tracking-tight uppercase">High-Conversion Draft</h3>
                          <div className="flex items-center gap-2 mt-1">
                            <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
                            <span className="text-[10px] text-gray-400 font-medium uppercase tracking-wider">Strategy Confidence: {proposal.proposal.score}%</span>
                          </div>
                        </div>
                      </div>
                      <button 
                        onClick={handleCopy}
                        className={`flex items-center gap-2 px-4 py-2 rounded-lg text-xs font-bold transition-all border ${copied ? 'bg-green-500/10 border-green-500/50 text-green-400' : 'bg-white/5 border-white/10 text-gray-400 hover:text-white hover:border-white/20'}`}
                      >
                        {copied ? 'COPIED!' : 'COPY DRAFT'}
                      </button>
                    </div>

                    <div className="bg-black/30 border border-white/5 rounded-2xl p-6 mb-8 min-h-[400px]">
                      <p className="text-gray-200 whitespace-pre-wrap leading-relaxed text-sm">
                        {proposal.proposal.draft}
                      </p>
                    </div>

                    <div className="space-y-4">
                      <div className="flex justify-between items-center">
                        <span className="text-[10px] font-bold text-gray-500 tracking-widest uppercase">Optimized Intelligence</span>
                        <span className="text-xs font-mono text-primary font-bold">{proposal.proposal.score}%</span>
                      </div>
                      <div className="progress-bar">
                        <motion.div 
                          initial={{ width: 0 }}
                          animate={{ width: `${proposal.proposal.score}%` }}
                          className="progress-fill"
                        />
                      </div>

                      {!proposal.status_updated && (
                        <div className="flex gap-3 pt-4">
                          <button 
                            onClick={() => handleUpdateStatus(proposal.proposal_id, 'won')}
                            className="flex-1 py-3 rounded-xl border border-green-500/30 bg-green-500/5 text-green-400 text-xs font-bold uppercase hover:bg-green-500/10 transition-all flex items-center justify-center gap-2"
                          >
                            <Sparkles size={14} /> Won Job
                          </button>
                          <button 
                            onClick={() => handleUpdateStatus(proposal.proposal_id, 'lost')}
                            className="flex-1 py-3 rounded-xl border border-white/10 bg-white/5 text-gray-400 text-xs font-bold uppercase hover:bg-white/10 transition-all"
                          >
                            Lost / No Reply
                          </button>
                        </div>
                      )}
                      {proposal.status_updated && (
                        <div className="pt-4 text-center">
                          <span className="text-[10px] text-primary font-bold uppercase tracking-widest">Feedback Received - Improving Synthesizer</span>
                        </div>
                      )}
                    </div>
                  </motion.div>
                ) : (
                  <div className="glass-card p-12 rounded-3xl h-full flex flex-col items-center justify-center text-center opacity-40 border-dashed">
                    <div className="w-16 h-16 rounded-full bg-white/5 flex items-center justify-center mb-6">
                      <Shield size={32} className="text-gray-600" />
                    </div>
                    <h3 className="text-lg font-bold text-gray-500 uppercase tracking-tighter">Awaiting Intelligence</h3>
                    <p className="text-sm text-gray-600 mt-2 max-w-xs">
                      Input the job details to activate the elite writing chain and generate a winning proposal.
                    </p>
                  </div>
                )}
              </AnimatePresence>
            </section>
          </div>
        )}

        {activeTab === 'knowledge' && (
          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="space-y-8"
          >
            <div className="flex justify-between items-end">
              <div>
                <h2 className="text-3xl font-bold uppercase tracking-tight">Knowledge Vault</h2>
                <p className="text-gray-500 mt-1">Enhance your proposals with corporate context and past successes.</p>
              </div>
              <button 
                className="p-2 bg-secondary/10 text-secondary rounded-xl hover:bg-secondary/20 transition-all flex items-center gap-2 px-4 text-xs font-bold uppercase cursor-pointer"
                onClick={() => {
                  const input = document.createElement('input')
                  input.type = 'file'
                  input.onchange = async (e: any) => {
                    const file = e.target.files[0]
                    const formData = new FormData()
                    formData.append('file', file)
                    await fetch('/api/knowledge/upload', {
                      method: 'POST',
                      body: formData
                    })
                    fetchKnowledge()
                  }
                  input.click()
                }}
              >
                <Plus size={16} /> Upload Context
              </button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {knowledgeItems.map((item, idx) => (
                <motion.div
                  key={item.id}
                  initial={{ opacity: 0, scale: 0.95 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ delay: idx * 0.05 }}
                  className="glass-card p-6 rounded-2xl flex flex-col group relative"
                >
                  <div className="flex justify-between items-start mb-4">
                    <div className="w-10 h-10 rounded-xl bg-secondary/10 flex items-center justify-center">
                      <Shield size={20} className="text-secondary" />
                    </div>
                    <button 
                      onClick={() => handleDeleteKnowledge(item.id)}
                      className="text-gray-600 hover:text-red-400 p-2"
                    >
                      <Trash2 size={16} />
                    </button>
                  </div>
                  <h3 className="text-lg font-bold text-white mb-2">{item.filename}</h3>
                  <p className="text-[10px] text-gray-500 uppercase tracking-widest mb-4">Type: {item.type || 'Context'}</p>
                  <div className="mt-auto pt-4 border-t border-white/5">
                    <span className="text-xs text-secondary font-mono">Active in Generation</span>
                  </div>
                </motion.div>
              ))}
              {knowledgeItems.length === 0 && (
                <div className="col-span-full py-20 glass-card rounded-3xl border-dashed flex flex-col items-center justify-center opacity-30">
                  <Shield size={48} className="mb-4" />
                  <p className="text-sm uppercase tracking-widest font-bold">Vault Empty</p>
                  <p className="text-xs text-gray-500 mt-2">Upload PDFs or Text files to give agents context.</p>
                </div>
              )}
            </div>
          </motion.div>
        )}

        {activeTab === 'portfolio' && (
          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="space-y-8"
          >
            <div className="flex justify-between items-end">
              <div>
                <h2 className="text-3xl font-bold uppercase tracking-tight">Project Portfolio</h2>
                <p className="text-gray-500 mt-1">Curated high-performance case studies.</p>
              </div>
              <div className="flex items-center gap-4">
                <button 
                  onClick={() => setIsAdding(true)}
                  className="p-2 bg-primary/10 text-primary rounded-xl hover:bg-primary/20 transition-all flex items-center gap-2 px-4 text-xs font-bold uppercase"
                >
                  <Plus size={16} /> Add Project
                </button>
                <div className="flex gap-2 bg-white/5 p-1 rounded-xl">
                {['All', 'AI', 'Web', 'Automation'].map(cat => (
                  <button
                    key={cat}
                    onClick={() => setActiveCategory(cat)}
                    className={`px-4 py-1.5 rounded-lg text-xs font-bold transition-all ${activeCategory === cat ? 'bg-primary text-white shadow-lg shadow-primary/20' : 'text-gray-500 hover:text-gray-300'}`}
                  >
                    {cat}
                  </button>
                ))}
              </div>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <AnimatePresence>
                {isAdding && (
                  <motion.div
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.9 }}
                    className="glass-card p-6 rounded-2xl flex flex-col border-primary/30"
                  >
                    <div className="flex justify-between items-center mb-4">
                      <span className="text-[10px] font-bold text-primary uppercase tracking-wider">{editId !== null ? 'Edit Project' : 'New Project'}</span>
                      <button onClick={() => { setIsAdding(false); setEditId(null); setNewProject({ title: '', category: 'AI', metrics: '', link: '', desc: '' }); }} className="text-gray-500 hover:text-white"><X size={16} /></button>
                    </div>
                    <input 
                      autoFocus
                      placeholder="Project Title"
                      className="bg-white/5 border border-white/10 rounded-lg p-2 text-sm text-white mb-2 focus:border-primary outline-none"
                      value={newProject.title}
                      onChange={e => setNewProject({...newProject, title: e.target.value})}
                    />
                    <select 
                      className="bg-white/5 border border-white/10 rounded-lg p-2 text-sm text-white mb-2 focus:border-primary outline-none"
                      value={newProject.category}
                      onChange={e => setNewProject({...newProject, category: e.target.value})}
                    >
                      <option value="AI">AI</option>
                      <option value="Web">Web</option>
                      <option value="Automation">Automation</option>
                    </select>
                    <input 
                      placeholder="Key Metric (e.g. $10k+ Revenue)"
                      className="bg-white/5 border border-white/10 rounded-lg p-2 text-sm text-white mb-2 focus:border-primary outline-none"
                      value={newProject.metrics}
                      onChange={e => setNewProject({...newProject, metrics: e.target.value})}
                    />
                    <textarea 
                      placeholder="Brief Description"
                      rows={3}
                      className="bg-white/5 border border-white/10 rounded-lg p-2 text-sm text-white mb-4 focus:border-primary outline-none"
                      value={newProject.desc}
                      onChange={e => setNewProject({...newProject, desc: e.target.value})}
                    />
                    <button 
                      onClick={handleAddProject}
                      className="mt-auto w-full py-2 bg-primary text-white rounded-xl text-xs font-bold uppercase hover:shadow-lg hover:shadow-primary/20 transition-all"
                    >
                      Save Project
                    </button>
                  </motion.div>
                )}
              </AnimatePresence>

              {filteredPortfolio.map((item, idx) => (
                <motion.div
                  key={item.id}
                  layout
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, scale: 0.9 }}
                  transition={{ delay: idx * 0.1 }}
                  whileHover={{ y: -5 }}
                  className="glass-card p-6 rounded-2xl flex flex-col group relative overflow-hidden"
                >
                  <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-primary/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
                  <div className="flex justify-between items-start mb-4">
                    <span className="text-[10px] font-bold text-primary px-2 py-1 bg-primary/10 rounded-md uppercase tracking-wider">
                      {item.category}
                    </span>
                    <div className="flex items-center gap-2">
                      <button 
                        onClick={() => handleEdit(item)}
                        className="text-gray-600 hover:text-primary transition-colors"
                      >
                        <Edit2 size={16} />
                      </button>
                      <button 
                        onClick={() => handleDeleteProject(item.id)}
                        className="text-gray-600 hover:text-red-400 transition-colors"
                      >
                        <Trash2 size={16} />
                      </button>
                      <button 
                        onClick={() => {
                          navigator.clipboard.writeText(item.link)
                          setCopied(true)
                          setTimeout(() => setCopied(false), 2000)
                        }}
                        className="text-gray-600 hover:text-white transition-colors"
                      >
                        <ChevronRight size={18} />
                      </button>
                    </div>
                  </div>
                  <h3 className="text-lg font-bold text-white mb-2 leading-tight group-hover:text-primary transition-colors">
                    {item.title}
                  </h3>
                  <p className="text-sm text-gray-500 mb-6 flex-grow">
                    {item.desc}
                  </p>
                  <div className="mt-auto pt-4 border-t border-white/5 flex items-center justify-between">
                    <div className="flex items-center gap-2 text-green-400 text-xs font-bold uppercase">
                      <Zap size={12} /> {item.metrics}
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          </motion.div>
        )}
      </main>
    </div>
  )
}
