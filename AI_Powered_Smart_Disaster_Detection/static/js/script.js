const form = document.getElementById('reportForm');
const button = document.getElementById('submitBtn');
form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const status = document.getElementById('status'); status.textContent = '';
  button.disabled = true; button.textContent = 'Analyzing…';
  try {
    const response = await fetch('/api/report', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({location:document.getElementById('location').value.trim(), description:document.getElementById('description').value.trim()})});
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Could not analyze the report.');
    document.getElementById('hazard').textContent = data.primary_hazard;
    document.getElementById('urgency').textContent = data.urgency + ' priority';
    document.getElementById('reportId').textContent = data.report_id;
    document.getElementById('resultLocation').textContent = data.location;
    document.getElementById('matches').textContent = data.detected_hazards.join(', ');
    document.getElementById('notice').textContent = data.notice;
    const list = document.getElementById('tips'); list.replaceChildren();
    data.tips.forEach(tip => { const li = document.createElement('li'); li.textContent = tip; list.appendChild(li); });
    document.getElementById('empty').classList.add('hidden');
    document.getElementById('result').classList.remove('hidden');
  } catch (error) { status.textContent = error.message || 'Cannot connect. Check that the Python backend is running.'; }
  finally { button.disabled = false; button.innerHTML = 'Analyze report <span>↗</span>'; }
});
