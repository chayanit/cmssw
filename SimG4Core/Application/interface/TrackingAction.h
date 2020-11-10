#ifndef SimG4Core_TrackingAction_H
#define SimG4Core_TrackingAction_H

#include <set>

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimG4Core/Notification/interface/SimActivityRegistry.h"
#include "SimG4Core/Notification/interface/TrackInformationExtractor.h"

#include "G4UserTrackingAction.hh"

class EventAction;
class TrackWithHistory;
class BeginOfTrack;
class EndOfTrack;
class CMSSteppingVerbose;

class TrackingAction : public G4UserTrackingAction {
public:
  explicit TrackingAction(EventAction* ea, const edm::ParameterSet& ps, CMSSteppingVerbose*);
  ~TrackingAction() override;

  void PreUserTrackingAction(const G4Track* aTrack) override;
  void PostUserTrackingAction(const G4Track* aTrack) override;

  inline TrackWithHistory* currentTrackWithHistory() { return currentTrack_; }
  inline const G4Track* geant4Track() const { return g4Track_; }
  inline G4TrackingManager* getTrackManager() { return fpTrackingManager; }

  inline void addPrimary(unsigned int id) { primaryIDs_.insert(id); }
  inline bool isPrimary(unsigned int id) { return (primaryIDs_.count(id) > 0); }
  inline void clearPrimaries() { primaryIDs_.clear(); }

  SimActivityRegistry::BeginOfTrackSignal m_beginOfTrackSignal;
  SimActivityRegistry::EndOfTrackSignal m_endOfTrackSignal;

private:
  TrackInformationExtractor extractor_;
  EventAction* eventAction_;
  TrackWithHistory* currentTrack_;
  CMSSteppingVerbose* steppingVerbose_;
  const G4Track* g4Track_;
  bool checkTrack_;
  bool doFineCalo_;
  std::set<unsigned int> primaryIDs_;
};

#endif
